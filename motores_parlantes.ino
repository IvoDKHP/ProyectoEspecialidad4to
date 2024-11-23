// Variables globales
unsigned long inicio_millis = 0;  // Tiempo inicial sincronizado
unsigned long tiempo_objetivo = 0;  // Tiempo objetivo en milisegundos
unsigned long tiempo_espera = 3600000; // Tiempo de espera para volver a activar el sensor
unsigned long tiempo_restringuido = 900000; // Tiempo de inactividad de los sensores

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
int contador_sensor = 0;  // Contador de activaciones del sensor
const int max_activaciones = 10; // Máximo de activaciones permitidas

void setup() {
  // Configuración de pines
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(motorPin, OUTPUT);
  pinMode(parlante, OUTPUT);
  digitalWrite(motorPin, LOW);

  // Inicia comunicación serie
  Serial.begin(9600);
  while (!Serial) {
    ; // Espera a que el puerto serie esté disponible
  }

  // Leer los valores iniciales desde el puerto serie
  Serial.println("Esperando valores de inicio y objetivo...");
  while (Serial.available() == 0) {
    // Espera hasta que haya datos disponibles
  }

  // Leer el mensaje y dividir los valores recibidos
  String mensaje = Serial.readStringUntil('\n');
  int separador = mensaje.indexOf(','); // Encuentra la posición de la coma
  if (separador != -1) {
    // Extraer y convertir los valores
    inicio_millis = mensaje.substring(0, separador).toInt();
    tiempo_objetivo = mensaje.substring(separador + 1).toInt();
    Serial.print("Inicio sincronizado: ");
    Serial.println(inicio_millis);
    Serial.print("Tiempo objetivo: ");
    Serial.println(tiempo_objetivo);
  } else {
    Serial.println("Error: Formato inválido.");
  }
}

void loop() {
  // Calcula el tiempo actual en milisegundos desde el inicio del día
  unsigned long tiempo_actual = millis() + inicio_millis;

  // Verificar si el tiempo actual coincide exactamente con la hora objetivo
  if (tiempo_actual >= tiempo_objetivo && tiempo_actual < tiempo_objetivo + 1000) {
    Serial.println("¡Hora objetivo alcanzada! Activando el motor.");
    digitalWrite(motorPin, LOW); // Encender el motor
    noTone(parlante);           // Asegurarse de que el parlante esté apagado
    delay(1000);                // Mantener el motor encendido por 1 segundo
    digitalWrite(motorPin, HIGH); // Apagar el motor

    // Incrementar el contador
    contador_sensor += 1;
    Serial.print("Contador del sensor: ");
    Serial.println(contador_sensor);

    // Asegurarse de no ejecutar este bloque más de una vez por coincidencia
    delay(1000); // Pausa breve para evitar múltiples activaciones
  }

  // Verifica si está fuera del periodo restringido
  if (tiempo_actual < tiempo_objetivo - tiempo_restringuido || tiempo_actual >= tiempo_objetivo + tiempo_espera) {
    if (!enEspera) {
      // Verifica si no se ha alcanzado el máximo de activaciones
      if (contador_sensor < max_activaciones) {
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
          contador_sensor += 1;  // Incrementar el contador de activaciones

          // Enviar el contador al monitor serie
          Serial.print("Contador del sensor: ");
          Serial.println(contador_sensor);

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
        // Se ha alcanzado el máximo de activaciones
        Serial.println("Máximo de activaciones alcanzado. Motor deshabilitado.");
        digitalWrite(motorPin, HIGH); // Asegura que el motor esté apagado
        noTone(parlante);             // Asegura que el parlante esté apagado
      }
    } else {
      // Si está en espera, no realiza detecciones
      delay(100);
    }
  } else {
    // Verifica si ya pasó el periodo de espera
    if (tiempo_actual >= tiempo_objetivo + tiempo_espera) {
      enEspera = false; // Reinicia el estado para permitir nuevas detecciones
      Serial.println("Tiempo límite alcanzado: Sistema listo para reanudar.");
    } else {
      // Mantener en espera
      Serial.println("Sistema en espera debido al periodo restringido.");
      digitalWrite(motorPin, HIGH); // Asegura que el motor esté apagado
      noTone(parlante);            // Apaga el parlante (por si está activo)
    }
  }
}