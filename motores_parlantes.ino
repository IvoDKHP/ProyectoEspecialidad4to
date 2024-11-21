// Pines del HC-SR04
const int trigPin = 10;   // Pin Trig del sensor
const int echoPin = 9;    // Pin Echo del sensor

// Pines del motor y el parlante
const int motorPin = 13;  // Pin del motor
const int parlante = 6;   // Pin del parlante

// Umbral de distancia en centímetros
const int distanciaUmbral = 20;

// Variables de control
bool enEspera = false;    // Controla el tiempo de espera después de encender el motor

void setup() {
  // Configuración de pines
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(motorPin, OUTPUT);
  pinMode(parlante, OUTPUT);

  // Inicia comunicación serie
  Serial.begin(9600);
}

void loop() {
  if (!enEspera) {
    // Enviar un pulso desde el pin Trig
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    // Leer el tiempo del pulso reflejado en el pin Echo
    long duracion = pulseIn(echoPin, HIGH);

    // Calcular la distancia en centímetros
    int distancia = duracion * 0.034 / 2;

    if (distancia > 0 && distancia <= distanciaUmbral) {
      // Se detecta un objeto dentro del rango
      Serial.println("Objeto detectado: Motor encendido.");
      digitalWrite(motorPin, LOW); // Encender el motor
      noTone(parlante);           // Apagar el parlante
      delay(1000);                // Mantener el motor encendido 1 segundo
      digitalWrite(motorPin, HIGH); // Apagar el motor

      // Entrar en estado de espera
      enEspera = true;
      Serial.println("Esperando 5 segundos para permitir otra señal.");
      delay(5000); // Tiempo de espera
      enEspera = false;
    } else {
      // No se detecta un objeto dentro del rango
      Serial.println("No se detecta objeto: Sonando parlante.");
      digitalWrite(motorPin, HIGH); // Asegurar que el motor esté apagado
      tone(parlante, 1000);         // Sonar el parlante (1000 Hz)
      delay(500);                   // Sonar durante 500 ms
      noTone(parlante);             // Apagar el parlante
      delay(500);                   // Pausa de 500 ms
    }
  } else {
    // Si está en espera, no realiza detecciones
    delay(100);
  }
}

