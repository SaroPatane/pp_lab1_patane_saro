import json
import csv
import re


with open("C:\\Users\\Sarop\\OneDrive\\Escritorio\\Tecnicatura en programacion UTN\\Programacion I\\primer_parcial\\dt.json") as file:
    data = json.load(file)

# 1)
lista_jugadores = data["jugadores"]

#Muestra la lista de jugadores con sus posiciones

def mostrar_jugador(lista: list):
    
    for jugador in lista:
        print("{0} - {1}".format(jugador["nombre"], jugador["posicion"]))
        #Use un for para que recorra el diccionario y el format para completar lo pedido

#----------------------------------------------------------------------------------------------

# 2)
def indice_jugador_estadisticas(lista:list):

    indice = 0

    for jugador in lista:
        indice += 1 #genero los indices con los cuales se elegira la opcion
        print(indice, "{0}".format(jugador["nombre"]))

    
    opcion = input("ingrese el indice (numero a la izquierda) del jugador del cual desee ver sus caracteristicas: ")
    while not opcion.isdigit(): #valido los indices del punto de arriba para que solo ingrese numeros
        opcion = input("reingrese solo el indice del jugador del cual desea ver sus caracteristicas: ")
    opcion = int(opcion)
    
    if opcion <= len(lista): #con la opcion indicada pido que imprima lo solicitado por consola
        jugador_seleccionado = lista[opcion - 1]
        print("{0} {1} {2}".format(jugador_seleccionado["nombre"], jugador_seleccionado["posicion"], jugador_seleccionado["estadisticas"]))
    
    else:
        print("opcion incorrecta")

#----------------------------------------------------------------------------------------------

# 3)

def estadisticas_jugador_in_csv(lista: list):

    indice = 0

    for jugador in lista:
        indice += 1 #vuelvo a generar los indices como en la funcion anterior
        print(indice, "{0}".format(jugador["nombre"]))
    
    opcion = int(input("ingrese el indice del jugador del cual desee ver sus caracteristicas: "))

    opcion = input("ingrese el indice (numero a la izquierda) del jugador del cual desee ver sus caracteristicas: ")
    while not opcion.isdigit(): #vuelvo a validar los indices del punto de arriba para que solo ingrese numeros
        opcion = input("reingrese solo el indice del jugador del cual desea ver sus caracteristicas: ")
    opcion = int(opcion)

    if opcion <= len(lista):
        #resto en 1 el numero ingresado para indicar el jugador correcto en la posicion indicada
        jugador_seleccionado = lista[opcion - 1] 
        nombre_jugador = jugador_seleccionado["nombre"]
        posicion_jugador = jugador_seleccionado["posicion"]
        estadisticas_jugador = jugador_seleccionado["estadisticas"]
        #pongo variables asignandoles los datos solicitados
    
        with open("lista_jugadores.csv", "w") as file: #creo el archivo csv con los datos solicitados
            archivo = csv.writer(file)
            archivo.writerow(["nombre", " posicion", " estadisticas"])
            archivo.writerow([nombre_jugador, posicion_jugador, estadisticas_jugador])
            

        print("las estadisticas del jugador seleccionado se guardaron en lista_jugadores.csv")
        #esto se imprime por consola si fue todo correcto
    else:

        print("opcion incorrecta")

# ---------------------------------------------------------------------------------------------

#4)

def indice_jugador_logros(lista:list):

    indice = 0

    for jugador in lista:
        indice += 1 #indico los indices en cada jugador
        print(indice, "{0}".format(jugador["nombre"]))
    
    opcion = int(input("ingrese el indice del jugador del cual desee ver sus logros: "))
    while not opcion.isdigit(): #valido los indices del punto de arriba para que solo ingrese numeros
        opcion = input("reingrese solo el indice del jugador del cual desea ver sus caracteristicas: ")
    opcion = int(opcion)
    
    if opcion <= len(lista):
        jugador_seleccionado = lista[opcion - 1] #resto en 1 para dar con la posicion correcta del jugador ingresado
        print("{0} {1}".format(jugador_seleccionado["nombre"], jugador_seleccionado["logros"]))
    else:
        print("opcion incorrecta")


#----------------------------------------------------------------------------------------------

#5)

def promedio_puntos_partido(lista:list):

    promedios_puntos = {}  
    for jugador in lista: 
        promedio_puntos = jugador["estadisticas"]["promedio_puntos_por_partido"]
        promedios_puntos[jugador["nombre"]] = promedio_puntos
    #creo un diccionario vacio y uso un for para asignar claves y valor sobre el nombre y el promedio de puntos
    
    claves = list(promedios_puntos.keys()) #creo una lista con las claves asignadas en el for

    #obtengo longitud y ordeno las claves utilizando ordenamiento burbuja
    cantidad_claves = len(claves) 
    for i in range(cantidad_claves-1): 
        for j in range(0, cantidad_claves-i-1):
            if promedios_puntos[claves[j]] > promedios_puntos[claves[j+1]]:
                claves[j], claves[j+1] = claves[j+1], claves[j]     

    
    diccionario_ordenado = {}
    for clave in claves:# sobre el diccinario vacio, itero sobre cada clave y se le asigna el valor correspondiente
        diccionario_ordenado[clave] = promedios_puntos[clave]
    
    return print(diccionario_ordenado)


#-------------------------------------------------------------------------------------------------

#6)

def jugador_en_salon_fama(lista:list):

    indice = 0

    for jugador in lista:
        indice += 1 
        print(indice, "{0}".format(jugador["nombre"]))
    #imprimo los indices y los nombres
    player = input("ingrese el nombre del jugador para chequear si esta dentro del salon de la fama o no (si no obtiene respuesta, no se encuentra dentro del salon de la fama): ")
    while not isinstance(player, str): #valido los indices del punto de arriba para que solo ingrese numeros
        player = input("reingrese solo el el nombre completo del jugador para ver si se encuentra o no del salon de la fama del baloncesto: ")
    player = player.title()
    #valido para que solo se ingresen datos str y el title() para que cada primera letra de cada palabra se escriba en mayuscula
    for jugador in lista:
        if jugador["nombre"] == player:
            for logro in jugador["logros"]:
                if logro == "Miembro del Salon de la Fama del Baloncesto":
                    print("el jugador ingresado es miembro del salon de la fama")
                    #itero sobre la lista y si tiene escrito en logros, el logro deseado, se imprime el mensaje que es miembro               

#------------------------------------------------------------------------------------------------

#7)

def rebotes_totales(lista:list):

    
    mayor_cantidad_rebotes = 0
    #inicializo la variable e itero sobre la lista
    for jugador in lista:
        if jugador["estadisticas"]["rebotes_totales"] > mayor_cantidad_rebotes:
            jugador_mayor_rebotes = jugador["nombre"]
            mayor_cantidad_rebotes = jugador["estadisticas"]["rebotes_totales"]
            #una vez encontrado el jugador le asigno una variable para el nombre y otro para la cantidad y los imprimo por consola usando print y format
    return "el jugador con mayor rebotes es {0} con {1} rebotes".format(jugador_mayor_rebotes, mayor_cantidad_rebotes)


#---------------------------------------------------------------------------------------------------

#8)

def mayor_tiros_campo(lista:list):

    #mismo sistema que el punto 7
    mayor_cantidad_tiros_campo = 0

    for jugador in lista:
        if jugador["estadisticas"]["porcentaje_tiros_de_campo"] > mayor_cantidad_tiros_campo:
            jugador_mayor_tiros_campo = jugador["nombre"]
            mayor_cantidad_tiros_campo = jugador["estadisticas"]["porcentaje_tiros_de_campo"]

    return print("el jugador con mayor tiros de campo es {0} con un porcentaje de {1} tiros".format(jugador_mayor_tiros_campo, mayor_cantidad_tiros_campo))

#---------------------------------------------------------------------------------------------------

#9)

def jugador_mayor_asistencias(lista:list):

    #mismo sistema que el punto 7 y 8
    mayor_cantidad_asistencias = 0

    for jugador in lista:
        if jugador["estadisticas"]["asistencias_totales"] > mayor_cantidad_asistencias:
            jugador_mayor_asistencias = jugador["nombre"]
            mayor_cantidad_asistencias = jugador["estadisticas"]["asistencias_totales"]

    return print("el jugador con mayor asistencias es {0} con una cantidad de {1} asistencias".format(jugador_mayor_asistencias, mayor_cantidad_asistencias))


#---------------------------------------------------------------------------------------------------

#10)

def jugador_mas_puntos_partido(lista:list):

    valor_ingresado = int(input("ingrese un valor: "))
    #ingreso un valor, lo normalizo a int e itero sobre la lista para imprimir los nombres mayor al valor ingresado
    for jugador in lista:
        if jugador["estadisticas"]["promedio_puntos_por_partido"] > valor_ingresado:
            print(jugador["nombre"])

#---------------------------------------------------------------------------------------------------

#11)

def jugador_mas_rebotes_partido(lista:list):

    #mismo sistema usado que en la funcion 10
    valor_ingresado = int(input("ingrese un valor: "))

    for jugador in lista:
        if jugador["estadisticas"]["promedio_rebotes_por_partido"] > valor_ingresado:
            print(jugador["nombre"])
            
#---------------------------------------------------------------------------------------------------

#12)

def jugador_mas_asistencias_partido(lista:list):

    #mismo sistema usado en funciones 10 y 11
    valor_ingresado = int(input("ingrese un valor: "))

    for jugador in lista:
        if jugador["estadisticas"]["promedio_asistencias_por_partido"] > valor_ingresado:
            print(jugador["nombre"])


#---------------------------------------------------------------------------------------------------

#13)

def jugador_mayor_robos_totales(lista:list):

    #mismo sistema usado en funciones 7 ,8 y 9
    mayor_cantidad_robos = 0

    for jugador in lista:
        if jugador["estadisticas"]["robos_totales"] > mayor_cantidad_robos:
            jugador_mayor_robos_totales = jugador["nombre"]
            mayor_cantidad_robos = jugador["estadisticas"]["robos_totales"]

    return print("el jugador con mayor robos totales es {0} con una cantidad de {1} robos".format(jugador_mayor_robos_totales, mayor_cantidad_robos))

#-----------------------------------------------------------------------------------------------------

#14)

def jugador_mayor_bloqueos_totales(lista:list):

    #mismo sistema usado en funcion 13
    mayor_cantidad_bloqueos = 0

    for jugador in lista:
        if jugador["estadisticas"]["bloqueos_totales"] > mayor_cantidad_bloqueos:
           jugador_mayor_bloqueos_totales = jugador["nombre"]
           mayor_cantidad_bloqueos = jugador["estadisticas"]["bloqueos_totales"]

    return print("el jugador con mayor bloqueos totales es {0} con una cantidad de {1} bloqueos".format(jugador_mayor_bloqueos_totales, mayor_cantidad_bloqueos))

#----------------------------------------------------------------------------------------------------- 

#15)


def jugador_mayor_tiros_libres(lista:list):

    #mismo sistema usado en funcion 12
    valor_ingresado = int(input("ingrese un valor: "))

    for jugador in lista:
        if jugador["estadisticas"]["porcentaje_tiros_libres"] > valor_ingresado:
            print(jugador["nombre"])


#------------------------------------------------------------------------------------------------------ 

#16)

def promedio_puntos_partido_sin_puntaje_mas_bajo(lista:list):

    promedios_puntos = {}
    for jugador in lista: #itero sobre la lista, asigno claves y valores
        promedio_puntos = jugador["estadisticas"]["promedio_puntos_por_partido"]
        promedios_puntos[jugador["nombre"]] = promedio_puntos

    # Obtengo el jugador con el menor puntaje 
    jugador_menor_puntos = min(promedios_puntos, key=promedios_puntos.get)
    menor_puntos = promedios_puntos[jugador_menor_puntos]

    # Creo el nuevo diccionario sin el jugador con el menor puntaje
    diccionario_ordenado = {}
    for jugador, promedio_puntos in promedios_puntos.items():
        if promedio_puntos > menor_puntos:
            diccionario_ordenado[jugador] = promedio_puntos
    
    return print(diccionario_ordenado)


#-------------------------------------------------------------------------------------------------------

#17)

def jugador_mayor_logros(lista:list):

    max_logros = 0
    #itero sobre la lista y asigno 2 variables, una para el nombre del jugadory otra para la mayor cantidad de logros (usando len para saber la cantidad)
    for jugador in lista:
        cantidad_logros = (len(jugador["logros"]))
        if cantidad_logros > max_logros:
            jugador_mayor_logros = jugador["nombre"]
            max_logros = cantidad_logros

    resultado = print("el jugador con mayor logros es {0} con {1} logros".format(jugador_mayor_logros, max_logros))

    return resultado

#------------------------------------------------------------------------------------------------------- 

#18)

def jugador_mayor_tiros_triples(lista:list):

    valor_ingresado = int(input("ingrese un valor: "))

    for jugador in lista:
        if jugador["estadisticas"]["porcentaje_tiros_triples"] > valor_ingresado:
            print(jugador["nombre"])

#--------------------------------------------------------------------------------------------------------

#19)

def jugador_mayor_temporadas(lista:list):
    
    mayor_cantidad_temporadas = 0

    for jugador in lista:
        if jugador["estadisticas"]["temporadas"] > mayor_cantidad_temporadas:
            jugador_mayor_temporadas = jugador["nombre"]
            mayor_cantidad_temporadas = jugador["estadisticas"]["temporadas"]

        return print("el jugador con mayor temporadas totales es {0} con una cantidad de {1} temporadas".format(jugador_mayor_temporadas, mayor_cantidad_temporadas))


#-------------------------------------------------------------------------------------------------------- 


#20)

def jugadores_mayores_tiros_de_campo(lista:list):

    for jugador in lista:
        print("{0}: {1}".format(jugador["nombre"], jugador["posicion"]))
    #imprimo la lista de jugadores con sus posiciones y luego las compara con el valor ingresado, para ver si cumple con el if, imprima los nombres correspondientes
    valor_ingresado = int(input("ingrese un valor: "))
    
    if valor_ingresado > jugador["estadisticas"]["promedio_asistencias_por_partido"]:
            print(jugador["nombre"])

  
#------------------------------------------------------------------------------------------------------- 


def bonus(lista:list):

    #creo 4 diccionarios vacios
    puntos = {}
    rebotes = {}
    asistencias = {}
    robos = {}
    
    #se les asigna clave y valor
    for jugador in lista:
        nombre = jugador["nombre"]
        puntos[nombre] = jugador["estadisticas"]["puntos_totales"]
        rebotes[nombre] = jugador["estadisticas"]["rebotes_totales"]
        asistencias[nombre] = jugador["estadisticas"]["asistencias_totales"]
        robos[nombre] = jugador["estadisticas"]["robos_totales"]
    
    #utilizo sorted para ordenar los datos de los diccionarios, uso key para iterar sobre los valores y reverse para darle un orden descendente
    ranking_puntos = sorted(puntos, key=puntos.get, reverse=True)
    ranking_rebotes = sorted(rebotes, key=rebotes.get, reverse=True)
    ranking_asistencias = sorted(asistencias, key=asistencias.get, reverse=True)
    ranking_robos = sorted(robos, key=robos.get, reverse=True)

    posiciones = {}
    for i, jugador in enumerate(ranking_puntos): #uso enumerate para iterar sobre el indice y el elemento
        posiciones[jugador] = [i+1, ranking_rebotes.index(jugador)+1, ranking_asistencias.index(jugador)+1, ranking_robos.index(jugador)+1]
    #Se asigna a cada jugador en posiciones una lista que contiene su posicion en cada ranking. Se utiliza el indice i para calcular la posicion en el ranking de puntos, y las funciones index()  para obtener la posición en los rankings de rebotes, asistencias y robos según el jugador.
    
    ruta_archivo_csv = "resultados.csv"
    #defino la ruta del csv y creo una lista de encabezados
    encabezados = ["Jugador", "Puntos", "Rebotes", "Asistencias", "Robos"]
    
    datos_csv = []

    for jugador in posiciones:
        fila = [jugador] + posiciones[jugador]
        datos_csv.append(fila)
        #ingreso los datos a la lista csv
    with open(ruta_archivo_csv, "w", newline="") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(encabezados)
        escritor_csv.writerows(datos_csv)
    #abro el archivo csv en modo escritura y le ingreso los datos de los encabezados y los datos asignados a cada uno
    

#------------------------------------------------------------------------------------------------------ 

#examen parcial extra:

#1)
def jugadores_por_cada_posicion(lista:list):

    contador_escolta = 0
    contador_base = 0
    contador_ala_pivot = 0
    contador_alero = 0
    contador_pivot = 0

    for jugador in lista:
        posicion = jugador["posicion"]
        if posicion == "Escolta":
            contador_escolta += 1
        elif posicion == "Base":
            contador_base += 1
        elif posicion == "Ala-Pivot":
            contador_ala_pivot += 1
        elif posicion == "Alero":
            contador_alero += 1
        elif posicion == "Pivot":
            contador_pivot += 1
        

    print("Contador Escolta:", contador_escolta)
    print("Contador Base:", contador_base)
    print("Contador Ala-Pivot:", contador_ala_pivot)
    print("Contador Alero:", contador_alero)
    print("Contador Pivot:", contador_pivot)


#--------------------------------------------------------------------------------------------------------

#2)
def mostrar_jugadores_all_star(lista):
    for jugador in lista:
        nombre = jugador['nombre']
        logros = jugador['logros']
        contador_all_star = 0

        for logro in logros:
            match = re.search(r"([0-9]+) veces All-Star", logro)
            if match:
                contador_all_star += int(match.group(1))

        return "{0}: {1} All-Star".format(nombre, contador_all_star)
    

#------------------------------------------------------------------------------------------------------- 


#3)

def mostrar_jugadores_con_mejores_estadisticas(lista:list[dict]):

    
    mejor_temporadas = {'jugador': None, 'valor': 0}
    mejor_puntos_totales = {'jugador': None, 'valor': 0}
    mejor_promedio_puntos_por_partido = {'jugador': None, 'valor': 0}
    mejor_rebotes_totales = {'jugador': None, 'valor': 0}
    mejor_promedio_rebotes_por_partido = {'jugador': None, 'valor': 0}
    mejor_asistencias_totales = {'jugador': None, 'valor': 0}
    mejor_promedio_asistencias_por_partido = {'jugador': None, 'valor': 0}
    mejor_robos_totales = {'jugador': None, 'valor': 0}
    mejor_bloqueos_totales = {'jugador': None, 'valor': 0}
    mejor_porcentaje_tiros_de_campo = {'jugador': None, 'valor': 0}
    mejor_porcentaje_tiros_libres = {'jugador': None, 'valor': 0}
    mejor_porcentaje_tiros_triples = {'jugador': None, 'valor': 0}
    

    
    for jugador in lista:
        estadisticas = jugador['estadisticas']
        nombre = jugador['nombre']
    
        if estadisticas['temporadas'] > mejor_temporadas['valor']:
            mejor_temporadas['jugador'] = nombre
            mejor_temporadas['valor'] = estadisticas['temporadas']

        
        elif estadisticas['puntos_totales'] > mejor_puntos_totales['valor']:
            mejor_puntos_totales['jugador'] = nombre
            mejor_puntos_totales['valor'] = estadisticas['puntos_totales']
        
        elif estadisticas['promedio_puntos_por_partido'] > mejor_promedio_puntos_por_partido['valor']:
            mejor_promedio_puntos_por_partido['jugador'] = nombre
            mejor_promedio_puntos_por_partido['valor'] = estadisticas['promedio_puntos_por_partido']
        
        elif estadisticas['rebotes_totales'] > mejor_rebotes_totales['valor']:
            mejor_rebotes_totales['jugador'] = nombre
            mejor_rebotes_totales['valor'] = estadisticas['rebotes_totales']
        
        elif estadisticas['promedio_rebotes_por_partido'] > mejor_promedio_rebotes_por_partido['valor']:
            mejor_promedio_rebotes_por_partido['jugador'] = nombre
            mejor_promedio_rebotes_por_partido['valor'] = estadisticas['promedio_rebotes_por_partido']
        
        elif estadisticas['asistencias_totales'] > mejor_asistencias_totales['valor']:
            mejor_asistencias_totales['jugador'] = nombre
            mejor_asistencias_totales['valor'] = estadisticas['asistencias_totales']
        
        elif estadisticas['promedio_asistencias_por_partido'] > mejor_promedio_asistencias_por_partido['valor']:
            mejor_promedio_asistencias_por_partido['jugador'] = nombre
            mejor_promedio_asistencias_por_partido['valor'] = estadisticas['promedio_asistencias_por_partido']
        
        elif estadisticas['robos_totales'] > mejor_robos_totales['valor']:
            mejor_robos_totales['jugador'] = nombre
            mejor_robos_totales['valor'] = estadisticas['robos_totales']
        
        elif estadisticas['bloqueos_totales'] > mejor_bloqueos_totales['valor']:
            mejor_bloqueos_totales['jugador'] = nombre
            mejor_bloqueos_totales['valor'] = estadisticas['bloqueos_totales']
        
        elif estadisticas['porcentaje_tiros_de_campo'] > mejor_porcentaje_tiros_de_campo['valor']:
            mejor_porcentaje_tiros_de_campo['jugador'] = nombre
            mejor_porcentaje_tiros_de_campo['valor'] = estadisticas['porcentaje_tiros_de_campo']
        
        elif estadisticas['porcentaje_tiros_libres'] > mejor_porcentaje_tiros_libres['valor']:
            mejor_porcentaje_tiros_libres['jugador'] = nombre
            mejor_porcentaje_tiros_libres['valor'] = estadisticas['porcentaje_tiros_libres']
        
        elif estadisticas['porcentaje_tiros_triples'] > mejor_porcentaje_tiros_triples['valor']:
            mejor_porcentaje_tiros_triples['jugador'] = nombre
            mejor_porcentaje_tiros_triples['valor'] = estadisticas['porcentaje_tiros_triples']

    print("Mayor cantidad de temporadas:", mejor_temporadas['jugador'], "(", mejor_temporadas['valor'], ")")
    print("Mayor cantidad de puntos totales:", mejor_puntos_totales['jugador'], "(", mejor_puntos_totales['valor'], ")") 
    print("Mayor cantidad de promedio puntos por partido:", mejor_promedio_puntos_por_partido['jugador'], "(", mejor_promedio_puntos_por_partido['valor'], ")") 
    print("Mayor cantidad de rebotes totales:", mejor_rebotes_totales['jugador'], "(", mejor_rebotes_totales['valor'], ")") 
    print("Mayor cantidad de promedio rebotes por partido:", mejor_promedio_rebotes_por_partido['jugador'], "(", mejor_promedio_rebotes_por_partido['valor'], ")") 
    print("Mayor cantidad de asistencias totales:", mejor_asistencias_totales['jugador'], "(", mejor_asistencias_totales['valor'], ")") 
    print("Mayor cantidad de promedio asistencias por partido:", mejor_promedio_asistencias_por_partido['jugador'], "(", mejor_promedio_asistencias_por_partido['valor'], ")") 
    print("Mayor cantidad de robos totales:", mejor_robos_totales['jugador'], "(", mejor_robos_totales['valor'], ")") 
    print("Mayor cantidad de bloqueos totales:", mejor_bloqueos_totales['jugador'], "(", mejor_bloqueos_totales['valor'], ")") 
    print("Mayor cantidad de porcentaje tiros de campo:", mejor_porcentaje_tiros_de_campo['jugador'], "(", mejor_porcentaje_tiros_de_campo['valor'], ")") 
    print("Mayor cantidad de porcentaje tiros libres:", mejor_porcentaje_tiros_libres['jugador'], "(", mejor_porcentaje_tiros_libres['valor'], ")") 
    print("Mayor cantidad de porcentaje tiros triples:", mejor_porcentaje_tiros_triples['jugador'], "(", mejor_porcentaje_tiros_triples['valor'], ")") 


#------------------------------------------------------------------------------------------------------- 

#4)

def mostrar_jugador_con_mejores_estadisticas(lista: list):
    mejor_temporadas = 0
    mejor_puntos_totales = 0
    mejor_promedio_puntos_por_partido = 0
    mejor_rebotes_totales = 0
    mejor_promedio_rebotes_por_partido = 0
    mejor_asistencias_totales = 0
    mejor_promedio_asistencias_por_partido = 0
    mejor_robos_totales = 0
    mejor_bloqueos_totales = 0
    mejor_porcentaje_tiros_de_campo = 0
    mejor_porcentaje_tiros_libres = 0
    mejor_porcentaje_tiros_triples = 0
    mejor_jugador = ""

    # Recorrer la lista de jugadores
    for jugador in data["jugadores"]:
        estadisticas = jugador["estadisticas"]

        # Comparar y actualizar las mejores estadísticas
        if estadisticas["temporadas"] > mejor_temporadas:
            mejor_temporadas = estadisticas["temporadas"]
            mejor_jugador = jugador["nombre"]

        if estadisticas["puntos_totales"] > mejor_puntos_totales:
            mejor_puntos_totales = estadisticas["puntos_totales"]
            mejor_jugador = jugador["nombre"]

        if estadisticas["promedio_puntos_por_partido"] > mejor_promedio_puntos_por_partido:
            mejor_promedio_puntos_por_partido = estadisticas["promedio_puntos_por_partido"]
            mejor_jugador = jugador["nombre"]

        if estadisticas["rebotes_totales"] > mejor_rebotes_totales:
            mejor_rebotes_totales = estadisticas["rebotes_totales"]
            mejor_jugador = jugador["nombre"]

        if estadisticas["promedio_rebotes_por_partido"] > mejor_promedio_rebotes_por_partido:
            mejor_promedio_rebotes_por_partido = estadisticas["promedio_rebotes_por_partido"]
            mejor_jugador = jugador["nombre"]

        if estadisticas["asistencias_totales"] > mejor_asistencias_totales:
            mejor_asistencias_totales = estadisticas["asistencias_totales"]
            mejor_jugador = jugador["nombre"]

        if estadisticas["promedio_asistencias_por_partido"] > mejor_promedio_asistencias_por_partido:
            mejor_promedio_asistencias_por_partido = estadisticas["promedio_asistencias_por_partido"]
            mejor_jugador = jugador["nombre"]

        if estadisticas["robos_totales"] > mejor_robos_totales:
            mejor_robos_totales = estadisticas["robos_totales"]
            mejor_jugador = jugador["nombre"]

        if estadisticas["bloqueos_totales"] > mejor_bloqueos_totales:
            mejor_bloqueos_totales = estadisticas["bloqueos_totales"]
            mejor_jugador = jugador["nombre"]

        if estadisticas["porcentaje_tiros_de_campo"] > mejor_porcentaje_tiros_de_campo:
            mejor_porcentaje_tiros_de_campo = estadisticas["porcentaje_tiros_de_campo"]
            mejor_jugador = jugador["nombre"]

        if estadisticas["porcentaje_tiros_libres"] > mejor_porcentaje_tiros_libres:
            mejor_porcentaje_tiros_libres = estadisticas["porcentaje_tiros_libres"]
            mejor_jugador = jugador["nombre"]

        if estadisticas["porcentaje_tiros_triples"] > mejor_porcentaje_tiros_triples:
            mejor_porcentaje_tiros_triples = estadisticas["porcentaje_tiros_triples"]
            mejor_jugador = jugador["nombre"]

    
    print("Mejor jugador:", mejor_jugador)

mostrar_jugador_con_mejores_estadisticas(lista_jugadores)

"""
while True:
    
    print("\nMenú de opciones, debe apretar alguna de las siguientes opciones para continuar:")
    print("1. Mostrar la lista de todos los jugadores del Dream Team")
    print("2. Seleccione un jugador por su índice para mostrar sus estadísticas completas")
    print("3. Seleccione un jugador por su índice para mostrar sus estadísticas completas y guardarlas en un archivo csv")
    print("4. Indique el indice del jugador del cual desea ver sus logros")
    print("5. Calcula y muestra el promedio de puntos por partido de todo el equipo del Dream Team")
    print("6. Ingresar el nombre de un jugador y mostrar si el mismo es miembro del Salón de la Fama del Baloncesto")
    print("7. Muestra el jugador con la mayor cantidad de rebotes totales")
    print("8. Muestra el jugador con el mayor porcentaje de tiros de campo")
    print("9. Muestra el jugador con la mayor cantidad de asistencias totales")
    print("10. Permite ingresar un valor para saber que jugadores han promediado más puntos por partido")
    print("11. Permite ingresar un valor para saber que jugadores han promediado más rebotes por partido")
    print("12. Permite ingresar un valor para saber que jugadores han promediado más asistencias por partido")
    print("13. Permite saber cual es el jugador con la mayor cantidad de robos totales")
    print("14. Permite saber cual es el jugador con la mayor cantidad de bloqueos totales")
    print("15. Permite ingresar un valor para saber que jugadores han promediado más tiros libres")
    print("16. Permite mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido")
    print("17. Muestra el jugador con la mayor cantidad de logros obtenidos")
    print("18. Permite ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor")
    print("19. Muestre el jugador con la mayor cantidad de temporadas jugadas")
    print("20. Permite ingresar un valor para saber que jugadores han hayan tenido un porcentaje de tiros de campo superior a ese valor")
    print("21. Bonus: ordena e importa a un archivo csv los puntos, rebotes, asistencias y robos de los jugadores")
    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")


    # Opción 1: Muestra la lista de todos los jugadores del Dream Team
    if opcion == "1":
        mostrar_jugador(lista_jugadores)

    # Opción 2: Selecciona un jugador por su índice para mostrar sus estadísticas completas
    elif opcion == "2":
        indice_jugador_estadisticas(lista_jugadores)
       
    # Opción 3: Selecciona un jugador por su índice para mostrar sus estadísticas completas y guardarlas en un archivo csv
    elif opcion == "3":
        estadisticas_jugador_in_csv(lista_jugadores)


    # Opción 4: Indica el indice del jugador del cual desea ver sus logros
    elif opcion == "4":
        indice_jugador_logros(lista_jugadores)


    # Opción 5: Calcula y muestra el promedio de puntos por partido de todo el equipo del Dream Team
    elif opcion == "5":
        promedio_puntos_partido(lista_jugadores)


    # Opción 6: Ingresar el nombre de un jugador y mostrar si el mismo es miembro del Salón de la Fama del Baloncesto
    elif opcion == "6":
        jugador_en_salon_fama(lista_jugadores)
    
    # Opcion 7: Muestra el jugador con la mayor cantidad de rebotes totales
    elif opcion == "7":
        rebotes_totales(lista_jugadores)
    
    # Opcion 8: Muestra el jugador con el mayor porcentaje de tiros de campo
    elif opcion == "8":
        mayor_tiros_campo(lista_jugadores)
    
    # Opcion 9: Muestra el jugador con la mayor cantidad de asistencias totales
    elif opcion == "9":
        jugador_mayor_asistencias(lista_jugadores)
    
    # Opcion 10: Permite ingresar un valor para saber que jugadores han promediado más puntos por partido
    elif opcion == "10":
        jugador_mas_puntos_partido(lista_jugadores)
    
    # Opcion 11: Permite ingresar un valor para saber que jugadores han promediado más rebotes por partido
    elif opcion == "11":
        jugador_mas_rebotes_partido(lista_jugadores)
    
    # Opcion 12: Permite ingresar un valor para saber que jugadores han promediado más asistencias por partido
    elif opcion == "12":
       jugador_mas_asistencias_partido(lista_jugadores)
    
    # Opcion 13: Permite saber cual es el jugador con la mayor cantidad de robos totales
    elif opcion == "13":
        jugador_mayor_robos_totales(lista_jugadores)
    
    # Opcion 14: Permite saber cual es el jugador con la mayor cantidad de bloqueos totales
    elif opcion == "14":
        jugador_mayor_bloqueos_totales(lista_jugadores)
    
    # Opcion 15: Permite ingresar un valor para saber que jugadores han promediado más tiros libres
    elif opcion == "15":
        jugador_mayor_tiros_libres(lista_jugadores)
    
    # Opcion 16: Permite mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido
    elif opcion == "16":
        promedio_puntos_partido_sin_puntaje_mas_bajo(lista_jugadores)
    
    # Opcion 17: Muestra el jugador con la mayor cantidad de logros obtenidos
    elif opcion == "17":
        jugador_mayor_logros(lista_jugadores)
    
    # Opcion 18: Permite ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor
    elif opcion == "18":
        jugador_mayor_tiros_triples(lista_jugadores)
    
    # Opcion 19: Muestre el jugador con la mayor cantidad de temporadas jugadas
    elif opcion == "19":
        jugador_mayor_temporadas(lista_jugadores)
    
    # Opcion 20: Permite ingresar un valor para saber que jugadores han hayan tenido un porcentaje de tiros de campo superior a ese valor
    elif opcion == "20":
        jugadores_mayores_tiros_de_campo(lista_jugadores)
    
    
    elif opcion == "21":
        bonus(lista_jugadores)


    # Opcion 0: Salir
    elif opcion == "0":
        break

    else:
        print("Opción inválida. Intente de nuevo.")


"""

