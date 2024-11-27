// Variables globales
unsigned long inicio_millis = 0;  // Tiempo inicial sincronizado

// Variables de control
int contador_sensor = 0;  // Contador de activaciones del sensor
int max_activaciones = 0; // Máximo de activaciones permitidas
int limite_cantidad = 7;  // cantidad de datos del array limites
int longitud_on_off;
int longitud_horarios;
int *limite;  // Puntero para el array 'limite'
int *on_off;  // Puntero para el array 'on_off'
int *horarios;  // Puntero para el array 'horarios'

// Pines del sensor 1
const int trigPin1 = 10;
const int echoPin1 = 9;

// Pines del sensor 2
const int trigPin2 = 4;
const int echoPin2 = 3;

// Umbral de distancia en centímetros
const int distanciaUmbral = 20;

// Pines del motor y el parlante
const int motorPin1 = 13;
const int motorPin2 = 12;
const int parlante = 6;

void prender_motor() {
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, LOW);
  delay(500);
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, LOW);
}

void enviar_senial1() {
  digitalWrite(trigPin1, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin1, LOW);
}

void setup() {
  // Inicia la comunicación serial
  Serial.begin(9600);

  // Espera hasta que haya datos disponibles
  while (!Serial) {
    // Espera
  }

  // Lee los primeros datos del serial
  if (Serial.available() >= 6) {  // Verifica que haya al menos 6 bytes disponibles
    unsigned long millisValue = Serial.parseInt();  // Recibe el valor de millis
    longitud_on_off = Serial.parseInt();   // Recibe el tamaño del primer array
    longitud_horarios = Serial.parseInt();   // Recibe el tamaño del segundo array

    // Asigna memoria dinámica para los arrays
    limite = new int[limite_cantidad];  // Tamaño fijo para 'limite'
    on_off = new int[longitud_on_off];   // Tamaño recibido desde el serial para 'on_off'
    horarios = new int[longitud_horarios];  // Tamaño recibido desde el serial para 'horarios'

    // Leer los datos para el array 'limite'
    for (int i = 0; i < limite_cantidad; i++) {
      if (Serial.available() > 0) {
        limite[i] = Serial.parseInt();  // Recibe el valor para el array 'limite'
      }
    }

    // Leer los datos para el array 'on_off'
    for (int i = 0; i < longitud_on_off; i++) {
      if (Serial.available() > 0) {
        on_off[i] = Serial.parseInt();  // Recibe el valor para el array 'on_off'
      }
    }

    // Leer los datos para el array 'horarios'
    for (int i = 0; i < longitud_horarios; i++) {
      if (Serial.available() > 0) {
        horarios[i] = Serial.parseInt();  // Recibe el valor para el array 'horarios'
      }
    }
  }

  // Configura los pines
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(parlante, OUTPUT);
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(echoPin2, INPUT);
  pinMode(trigPin2, INPUT);
}

void loop() {
  // El loop está vacío porque no hay más datos que recibir constantemente
}
