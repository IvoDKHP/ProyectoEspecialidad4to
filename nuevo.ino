// Variables globales
unsigned long inicio_millis = 0;  // Tiempo inicial sincronizado
int hora_actual = 0;  // <-- Se añadió el punto y coma

// Variables de control
int contador_sensor = 0;  // Contador de activaciones del sensor
int max_activaciones = 0; // Máximo de activaciones permitidas
int limite_cantidad = 7;  // cantidad de datos del array limites
int longitud_on_off;
int longitud_horarios;
int *limite;  // Puntero para el array 'limite'
int *on_off;  // Puntero para el array 'on_off'
int *horarios;  // Puntero para el array 'horarios'
int iterame = 0; // para iterarse
int iterame2 = 0;
bool comida = true;
int *horas_motor_lunes; // Punteros para los arrays de las horas del motor por día
int *horas_motor_martes;
int *horas_motor_miercoles;
int *horas_motor_jueves;
int *horas_motor_viernes;
int *horas_motor_sabado;
int *horas_motor_domingo;
int elementosActuales = 0;  // <-- Corregido el punto y coma
int valor = 0;  // <-- Corregido el punto y coma

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

void agregarValor_lunes(int valor) {
  // Redimensionar el array para agregar un nuevo elemento
  horas_motor_lunes = (int*)realloc(horas_motor_lunes, (elementosActuales + 1) * sizeof(int));
  
  // Agregar el nuevo valor
  horas_motor_lunes[elementosActuales] = valor;

  // Incrementar el contador de elementos
  elementosActuales++;
}

void agregarValor_martes(int valor) {
  // Redimensionar el array para agregar un nuevo elemento
  horas_motor_martes = (int*)realloc(horas_motor_martes, (elementosActuales + 1) * sizeof(int));
  
  // Agregar el nuevo valor
  horas_motor_martes[elementosActuales] = valor;

}

void agregarValor_miercoles(int valor) {
  // Redimensionar el array para agregar un nuevo elemento
  horas_motor_miercoles = (int*)realloc(horas_motor_miercoles, (elementosActuales + 1) * sizeof(int));
  
  // Agregar el nuevo valor
  horas_motor_miercoles[elementosActuales] = valor;

}

void agregarValor_jueves(int valor) {
  // Redimensionar el array para agregar un nuevo elemento
  horas_motor_jueves = (int*)realloc(horas_motor_jueves, (elementosActuales + 1) * sizeof(int));
  
  // Agregar el nuevo valor
  horas_motor_jueves[elementosActuales] = valor;
}

void agregarValor_viernes(int valor) {
  // Redimensionar el array para agregar un nuevo elemento
  horas_motor_viernes = (int*)realloc(horas_motor_viernes, (elementosActuales + 1) * sizeof(int));
  
  // Agregar el nuevo valor
  horas_motor_viernes[elementosActuales] = valor;

}

void agregarValor_sabado(int valor) {
  // Redimensionar el array para agregar un nuevo elemento
  horas_motor_sabado = (int*)realloc(horas_motor_sabado, (elementosActuales + 1) * sizeof(int));
  
  // Agregar el nuevo valor
  horas_motor_sabado[elementosActuales] = valor;
}

void agregarValor_domingo(int valor) {
  // Redimensionar el array para agregar un nuevo elemento
  horas_motor_domingo = (int*)realloc(horas_motor_domingo, (elementosActuales + 1) * sizeof(int));
  
  // Agregar el nuevo valor
  horas_motor_domingo[elementosActuales] = valor;

  // Incrementar el contador de elementos
  elementosActuales++;
}

void prender_parlante() {
  digitalWrite(parlante, HIGH);
  delay(1000);
  digitalWrite(parlante, LOW);
}

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
  long duracion1 = pulseIn(echoPin1, HIGH);
  int distancia1 = duracion1 * 0.034 / 2;
  if (distancia1 > 0 && distancia1 <= distanciaUmbral) {
    prender_motor();
  }
}

void enviar_senial2() {
  digitalWrite(trigPin2, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin2, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin2, LOW);
  long duracion2 = pulseIn(echoPin2, HIGH);
  int distancia2 = duracion2 * 0.034 / 2;
  if (distancia2 == 0 || distancia2 == INFINITY || distancia2 > distanciaUmbral) {
    prender_parlante();
    comida = false;
  }
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
    hora_actual = Serial.parseInt();  // <-- Se corrigió la declaración de 'hora_actual'
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
  pinMode(trigPin2, OUTPUT);
}

void loop() {
  while (comida) {
    enviar_senial2();
    if (hora_actual > on_off[iterame2]) {  // <-- Corregí el 'if'
      iterame2 = iterame2 + 1;
    } else if (hora_actual < on_off[iterame2]) {  // <-- Corregí el 'else if'
      if (iterame2 % 2 == 1) {  // <-- Corregí el operador '==' y la sintaxis
        enviar_senial1();
      }
    }

    if(hora_actual < 86400000 * 7) {  // <-- Corregí la comparación con el número 86400000
      if (horarios[iterame] < 86400000  * 7) {
        horarios[iterame] = valor;
        agregarValor_domingo(valor);  // <-- Corregí la llamada a la función
      }
    }

    if(hora_actual < 86400000 * 6) {  // <-- Corregí la comparación con el número 86400000
      if (horarios[iterame] < 86400000 * 6) {
        horarios[iterame] = valor;
        agregarValor_sabado(valor);  // <-- Corregí la llamada a la función
      }
    }
    
    if(hora_actual < 86400000 * 5) {  // <-- Corregí la comparación con el número 86400000
      if (horarios[iterame] < 86400000 * 5) {
        horarios[iterame] = valor;
        agregarValor_viernes(valor);  // <-- Corregí la llamada a la función
      }
    }

    if(hora_actual < 86400000 * 4) {  // <-- Corregí la comparación con el número 86400000
      if (horarios[iterame] < 86400000 *4) {
        horarios[iterame] = valor;
        agregarValor_jueves(valor);  // <-- Corregí la llamada a la función
      }
    }

    if(hora_actual < 86400000 * 3) {  // <-- Corregí la comparación con el número 86400000
      if (horarios[iterame] < 86400000 * 3) {
        horarios[iterame] = valor;
        agregarValor_miercoles(valor);  // <-- Corregí la llamada a la función
      }
    }

    if(hora_actual < 86400000 * 2) {  // <-- Corregí la comparación con el número 86400000
      if (horarios[iterame] < 86400000* 2) {
        horarios[iterame] = valor;
        agregarValor_martes(valor);  // <-- Corregí la llamada a la función
      }
    }

    if(hora_actual < 86400000) {  // <-- Corregí la comparación con el número 86400000
      if (horarios[iterame] < 86400000) {
        horarios[iterame] = valor;
        agregarValor_lunes(valor);  // <-- Corregí la llamada a la función
      }
    }

    if (hora_actual > horarios[iterame]) {  // <-- Corregí el nombre de la variable 'horario' a 'horarios'
      iterame = iterame + 1;
    } else if (hora_actual == horarios[iterame]) {  // <-- Corregí la comparación
      prender_motor();
      iterame = iterame + 1;
    }
  }
}