unsigned long customMillis = 0; // Variable global para almacenar el valor inicial
unsigned long offsetMillis = 0; // Diferencia entre millis() del Arduino y customMillis
unsigned long minutos = 0;  // Convierte el tiempo a minutos
bool time_millis = false; // Variables de control
bool long_pa_tm = false;
bool long_hr_tm = false;
bool list1_tm = false;
bool list2_tm = false;
bool list3_tm = false;
bool activacion = true;
bool activation1 = true;
int a = 1;
int contador_on_off = 0;
int contador_sensor_estats = 0;
int contador_sensor = 0;  // Contador de activaciones del sensor
int long_pa = 1; // Largos preseteados
int long_hr = 1;
unsigned long lista_hora_sensor[100];
unsigned long lista_contador_stats[50];
unsigned long lista_contador[50];
unsigned long list_pa[10]; // Listas
unsigned long list_hr[10];
int list_lm[10];
int dato = 0; // Dato de control
const int distanciaUmbral = 10; // Distancia umbral en cm
const int distanciaUmbral2 = 6;
// Pines de motores
const int motorPin1 = 13;
const int motorPin2 = 12;
// Pines del sensor 1
const int trigPin1 = 10;
const int echoPin1 = 9;
// Pines del sensor 2
const int trigPin2 = 4;
const int echoPin2 = 3;
//pines del parlante
const int parlante = 6;
unsigned long tiempoActual = 0; // Declaración global de tiempoActual
int currentSize = 0;  // Controlador para el tamaño actual del arreglo
int currentSize1 = 0;
int currentSize2 = 0;

void appendToList(int value) {
  // Añadir el valor al arreglo
  lista_contador_stats[currentSize] = value;
  currentSize++;  // Aumentar el contador de elementos almacenados
  Serial.print("Valor añadido: ");
  Serial.println(value);
}

void appendToList1(int value) {
  // Añadir el valor al arreglo
  lista_hora_sensor[currentSize1] = value;
  currentSize1++;  // Aumentar el contador de elementos almacenados
  Serial.print("Valor añadido: ");
  Serial.println(value);
}

void appendToList2(int value) {
  // Añadir el valor al arreglo
  lista_contador[currentSize2] = value;
  currentSize2++;  // Aumentar el contador de elementos almacenados
  Serial.print("Valor añadido: ");
  Serial.println(value);
}

void contador_reinicio() {
  // Lunes
  if (tiempoActual >= 0 && tiempoActual <= 1000) {
    Serial.println("Reinicio: Lunes, reiniciando contador.");
    appendToList2(contador_sensor);
    contador_sensor = 0; 
    appendToList(contador_sensor_estats);
    contador_sensor_estats = 0;
  }
  // Martes
  if (tiempoActual >= 86400000 && tiempoActual <= 86400000 + 1000) {
    Serial.println("Reinicio: Martes, reiniciando contador.");
    appendToList2(contador_sensor);
    contador_sensor = 0;
    appendToList(contador_sensor_estats);
    contador_sensor_estats = 0;
  }
  // Miércoles
  if (tiempoActual >= 86400000*2 && tiempoActual <= (86400000*2) + 1000) {
    Serial.println("Reinicio: Miércoles, reiniciando contador.");
    appendToList2(contador_sensor);
    contador_sensor = 0;
    appendToList(contador_sensor_estats);
    contador_sensor_estats = 0;
  }
  // Jueves
  if (tiempoActual >= 86400000*3 && tiempoActual <= (86400000*3) + 1000) {
    Serial.println("Reinicio: Jueves, reiniciando contador.");
    appendToList2(contador_sensor);
    contador_sensor = 0;
    appendToList(contador_sensor_estats);
    contador_sensor_estats = 0;
  }
  // Viernes
  if (tiempoActual >= 86400000*4 && tiempoActual <= (86400000*4) + 1000) {
    Serial.println("Reinicio: Viernes, reiniciando contador.");
    appendToList2(contador_sensor);
    contador_sensor = 0;
    appendToList(contador_sensor_estats);
    contador_sensor_estats = 0;
  }
  // Sábado
  if (tiempoActual >= 86400000*5 && tiempoActual <= (86400000*5) + 1000) {
    Serial.println("Reinicio: Sábado, reiniciando contador.");
    appendToList2(contador_sensor);
    contador_sensor = 0;
    appendToList(contador_sensor_estats);
    contador_sensor_estats = 0;
  }
  // Domingo
  if (tiempoActual >= 86400000*6 && tiempoActual <= (86400000*6) + 1000) {
    Serial.println("Reinicio: Domingo, reiniciando contador.");
    appendToList2(contador_sensor);
    contador_sensor = 0;
    appendToList(contador_sensor_estats);
    contador_sensor_estats = 0;
  }
}

void activar_sensor2(){
  digitalWrite(trigPin2, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin2, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin2, LOW);

  long duracion2 = pulseIn(echoPin2, HIGH);
  int distancia2 = duracion2 * 0.034 / 2;

  if (distancia2 == 0 || distancia2 == INFINITY || distancia2 > distanciaUmbral2) {
    Serial.println("Sensor 2 activado, distancia mayor que umbral.");
    prender_parlante();
  }
}

void prender_parlante() {
  Serial.println("Activando parlante.");
  tone(parlante, 2000);
  delay(500);
  noTone(parlante);
}

void prender_motores() {
  Serial.println("Motores activados.");
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, LOW);
  delay(400);
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, LOW);
}

void activar_sensor1() {
  // Evita comparar explícitamente con true
  // Enviar pulso ultrasónico
  digitalWrite(trigPin1, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin1, LOW);

  // Medir duración del eco
  long duracion1 = pulseIn(echoPin1, HIGH);
  int distancia1 = duracion1 * 0.034 / 2; // Convertir tiempo en distancia

  // Comprobar si la distancia está dentro del umbral
  if (distancia1 > 0 && distancia1 <= distanciaUmbral) {
    contador_sensor_estats = contador_sensor_estats + 1;
    if (activacion) {
      appendToList1(minutos);
      Serial.println("Sensor 1 activado, distancia dentro del umbral.");
      prender_motores(); // Activar motores si la distancia es válida
      contador_sensor = contador_sensor + 1; // Incrementar el contador
    }
  }
}

void recivir_valore() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    input.trim();

    if (!time_millis) {
      unsigned long tiempo = input.toInt();
      customMillis = tiempo;
      offsetMillis = millis();
      time_millis = true;
      Serial.println("Recibiendo valor de tiempo.");
    } else if (!long_pa_tm) {
      long_pa = input.toInt();
      long_pa_tm = true;
      Serial.println("Configurando largo preseteado (long_pa).");
    } else if (!long_hr_tm) {
      long_hr = input.toInt();
      long_hr_tm = true;
      Serial.println("Configurando largo horario (long_hr).");
    } else if (!list1_tm) {
      for (int i = 0; i < long_pa; i++) {
        dato = 0;
        while (dato == 0) {
          input = Serial.readStringUntil('\n');
          input.trim();
          dato = input.toInt();
          if (dato == -2) {
            dato = 0;
            break;
          }
        }
        list_pa[i] = dato;
        Serial.print("Valor de list_pa[" + String(i) + "]: ");
        Serial.println(list_pa[i]);
      }
      list1_tm = true;
    } else if (!list2_tm) {
      for (int i = 0; i < long_hr; i++) {
        dato = 0;
        while (dato == 0) {
          input = Serial.readStringUntil('\n');
          input.trim();
          dato = input.toInt();
          if (dato == -2) {
            dato = 0;
            break;
          }
        }
        list_hr[i] = dato;
        Serial.print("Valor de list_hr[" + String(i) + "]: ");
        Serial.println(list_hr[i]);
      }
      list2_tm = true;
    } else if (!list3_tm) {
      for (int i = 0; i < 7; i++) {
        dato = 0;
        while (dato == 0) {
          input = Serial.readStringUntil('\n');
          input.trim();
          dato = input.toInt();
          if (dato == -2) {
            dato = 0;
            break;
          }
        }
        list_lm[i] = dato;
        Serial.print("Valor de list_lm[" + String(i) + "]: ");
        Serial.println(list_lm[i]);
      }
      list3_tm = true;
      delay(1000);
      time_millis = false;
      long_pa_tm = false;
      long_hr_tm = false;
      list1_tm = false;
      list2_tm = false;
      list3_tm = false;
    }
  }
}

void contador_sensro() {
  //lunes
  if (tiempoActual < 86400000) {
    if (list_lm[0] == contador_sensor) {
      activacion = false;
      Serial.println("Sensor desactivado en lunes.");
    } else {
      activacion = true;
      contador_reinicio();
    }
  } //martes
  else if (tiempoActual > 86400000 && tiempoActual < 86400000 * 2 ) {
    if (list_lm[1] == contador_sensor) {
      activacion = false;
      Serial.println("Sensor desactivado en martes.");
    } else {
      activacion = true;
      contador_reinicio();
    }
  } //miercoles
  else if (tiempoActual > 86400000*2 && tiempoActual < 86400000 * 3 ) {
    if (list_lm[2] == contador_sensor) {
      activacion = false;
      Serial.println("Sensor desactivado en miércoles.");
    } else {
      activacion = true;
      contador_reinicio();
    }
  } //jueves
  else if (tiempoActual > 86400000*3 && tiempoActual < 86400000*4 ) {
    if (list_lm[3] == contador_sensor) {
      activacion = false;
      Serial.println("Sensor desactivado en jueves.");
    } else {
      activacion = true;
      contador_reinicio();
    }
  }//viernes
  else if (tiempoActual > 86400000*4 && tiempoActual < 86400000*5 ) {
    if (list_lm[4] == contador_sensor) {
      activacion = false;
      Serial.println("Sensor desactivado en viernes.");
    } else {
      activacion = true;
      contador_reinicio();
    }
  }//sabado
  else if (tiempoActual > 86400000*5 && tiempoActual < 86400000*6 ) {
    if (list_lm[5] == contador_sensor) {
      activacion = false;
      Serial.println("Sensor desactivado en sábado.");
    } else {
      activacion = true;
      contador_reinicio();
    }
  }//domingo
  else if (tiempoActual > 86400000*6 && tiempoActual < 86400000*7 ) {
    if (list_lm[6] == contador_sensor) {
      activacion = false;
      Serial.println("Sensor desactivado en domingo.");
    } else {
      activacion = true;
      contador_reinicio();
    }
  }
}

void setup() {
  Serial.begin(9600); // Inicia la comunicación serial
  pinMode(motorPin1, OUTPUT); // Pines motor
  pinMode(motorPin2, OUTPUT);
  pinMode(trigPin1, OUTPUT); // Configurar pines del sensor 1
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT); // Configurar pines sensor 2
  pinMode(echoPin2, INPUT);
  digitalWrite(motorPin1, LOW); // Apaga los pines del motor
  digitalWrite(motorPin2, LOW);
}

void horas_comida() {
  Serial.println(minutos);
  for (int i = 0; i < long_hr; i++) { // Recorrer la lista hasta long_hr
    if (minutos != 0) {
      if (list_hr[i]  == minutos) { // Comparar cada elemento con 'minutos'
        prender_motores(); // Llamar a la función si hay coincidencia
        minutos +=1;
        delay(60000);
        break; // Salir del bucle al encontrar una coincidencia
      }
    }
  }
}

void enviar_datos() {
}

void loop() {
  tiempoActual = customMillis + (millis() - offsetMillis); // Actualización del tiempo
  minutos = tiempoActual / 60000;  // Convierte el tiempo a minutos
  recivir_valore();
  horas_comida();
  contador_sensro();
  activar_sensor1();
  activar_sensor2();
  delay(1000); // Esperar 1 segundo antes de la siguiente iteración
}