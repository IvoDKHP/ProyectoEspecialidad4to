def organizar_horarios(matriz):
    nueva_matriz = [] # Creamos la matriz que vamos a utilizar para devolver los datos ordenados 
    for fila in matriz: 
        horarios_validos = [] # Creamos la lista de horarios x dia    
        for horario in fila:
            if horario != "0:0": # Filtrar los horarios válidos (diferentes de "0:0") y convertirlos a minutos
                horas, minutos = map(int, horario.split(":"))
                minutos_totales = horas * 60 + minutos #Obtiene los minutos correspondientes al horario
                horarios_validos.append((horario, minutos_totales)) #Agregamos la tupla a la lista de horarios validos 
        
        for i in range(len(horarios_validos) - 1): #Ordenar los horarios válidos por minutos
            for j in range(len(horarios_validos) - 1 - i): #Generar numero de pasadas necesarias para acomodar
                #Si el valor de la derecha es mayor que el izquierdo se intercambian
                if horarios_validos[j][1] > horarios_validos[j + 1][1]:
                    horarios_validos[j], horarios_validos[j + 1] = horarios_validos[j + 1], horarios_validos[j] 

        fila_ordenada = [] #Se crea la lista de horarios ordenados del dia
        for horario, minutos in horarios_validos:
            fila_ordenada.append(horario) #Agregar los horarios de forma ordenada a la lista

        fila_ordenada += ["0:0"] * (len(fila) - len(fila_ordenada)) #Añade los "0:0" al final de la lista (compara cuantos son los faltantes)

        nueva_matriz.append(fila_ordenada) #Agrega la lista ordenada a la nueva matriz

    return nueva_matriz  # Devolver la nueva matriz ya ordenada