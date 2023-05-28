import json
import re
import csv


with open("C:\\Users\\Sarop\\OneDrive\\Escritorio\\Tecnicatura en programacion UTN\\Programacion I\\primer_parcial\\dt.json") as file:
    data = json.load(file)

# 1)
lista_jugadores = data["jugadores"]

def mostrar_jugador(lista: list):
    
    for jugador in lista:
        print("{0} - {1}".format(jugador["nombre"], jugador["posicion"]))

#----------------------------------------------------------------------------------------------

# 2)
def indice_jugador_estadisticas(lista:list):

    indice = 0

    for jugador in lista:
        indice += 1
        print(indice, "{0}".format(jugador["nombre"]))
    
    opcion = int(input("ingrese el indice del jugador del cual desee ver sus caracteristicas: "))
    
    if opcion <= len(lista):
        jugador_seleccionado = lista[opcion - 1]
        print("{0} {1} {2}".format(jugador_seleccionado["nombre"], jugador_seleccionado["posicion"], jugador_seleccionado["estadisticas"]))
    
    else:
        print("opcion incorrecta")

#----------------------------------------------------------------------------------------------

# 3)

def estadisticas_jugador_in_csv(lista: list):

    indice = 0

    for jugador in lista:
        indice += 1
        print(indice, "{0}".format(jugador["nombre"]))
    
    opcion = int(input("ingrese el indice del jugador del cual desee ver sus caracteristicas: "))

    if opcion <= len(lista):
        jugador_seleccionado = lista[opcion - 1]
        nombre_jugador = jugador_seleccionado["nombre"]
        posicion_jugador = jugador_seleccionado["posicion"]
        estadisticas_jugador = jugador_seleccionado["estadisticas"]
    
        with open("lista_jugadores.csv", "w") as file:
            archivo = csv.writer(file)
            archivo.writerow(["nombre", " posicion", " estadisticas"])
            archivo.writerow([nombre_jugador, posicion_jugador, estadisticas_jugador])
            

        print("las estadisticas del jugador seleccionado se guardaron en lista_jugadores.csv")

    else:

        print("opcion incorrecta")

# ---------------------------------------------------------------------------------------------

#4)

def indice_jugador_logros(lista:list):

    indice = 0

    for jugador in lista:
        indice += 1
        print(indice, "{0}".format(jugador["nombre"]))
    
    opcion = int(input("ingrese el indice del jugador del cual desee ver sus logros: "))
    
    if opcion <= len(lista):
        jugador_seleccionado = lista[opcion - 1]
        print("{0} {1}".format(jugador_seleccionado["nombre"], jugador_seleccionado["logros"]))
    else:
        print("opcion incorrecta")


#----------------------------------------------------------------------------------------------

#5)

def promedio_puntos_partido(lista:list):

    cantidad_puntos = 0
    lista_desordenada = []
    lista_iz = []
    lista_de = []

    for jugador in lista:
        puntos = jugador["estadisticas"]["promedio_puntos_por_partido"]
        cantidad_puntos += puntos
        lista_desordenada.append(cantidad_puntos)
        if len(lista_desordenada) <= 1:
            return lista_desordenada
        else:
            pivot = lista_desordenada[0]
            for elemento in lista_desordenada[1:]:
                if elemento > pivot:
                    lista_de.append(elemento)
                else:
                    lista_iz.append(elemento)
        lista_iz = promedio_puntos_partido(lista_iz, True)
        lista_iz.append(pivot)
        lista_de = promedio_puntos_partido(lista_de, True)
        lista_iz.extend(lista_de)

    promedio_total = cantidad_puntos / len(lista)
    print(lista_iz, "promedio:", promedio_total)
    return lista_iz
            

promedio_puntos_partido(lista_jugadores)

#-------------------------------------------------------------------------------------------------

#6)

def jugador_en_salon_fama(lista:list):

    indice = 0

    for jugador in lista:
        indice += 1
        print(indice, "{0}".format(jugador["nombre"]))
    
    player = input("ingrese el nombre del jugador para chequear si esta dentro del salon de la fama o no (si no obtiene respuesta, no se encuentra dentro del salon de la fama): ")
    player = player.title()

    for jugador in lista:
        if jugador["nombre"] == player:
            for logro in jugador["logros"]:
                if logro == "Miembro del Salon de la Fama del Baloncesto":
                    print("el jugador ingresado es miembro del salon de la fama")
                else:
                    return False  
                    

#------------------------------------------------------------------------------------------------

#7)

def rebotes_totales(lista:list):

    jugador_mayor_rebotes = ""
    mayor_cantidad_rebotes = 0

    for jugador in lista:
        if jugador["estadisticas"]["rebotes_totales"] > mayor_cantidad_rebotes:
            jugador_mayor_rebotes = jugador["nombre"]
            mayor_cantidad_rebotes = jugador["estadisticas"]["rebotes_totales"]

    return print("el jugador con mayor rebotes es {0} con {1} rebotes".format(jugador_mayor_rebotes, mayor_cantidad_rebotes))


#---------------------------------------------------------------------------------------------------

#8)

def mayor_tiros_campo(lista:list):

    jugador_mayor_tiros_campo = ""
    mayor_cantidad_tiros_campo = 0

    for jugador in lista:
        if jugador["estadisticas"]["porcentaje_tiros_de_campo"] > mayor_cantidad_tiros_campo:
            jugador_mayor_tiros_campo = jugador["nombre"]
            mayor_cantidad_tiros_campo = jugador["estadisticas"]["porcentaje_tiros_de_campo"]

    return print("el jugador con mayor tiros de campo es {0} con un porcentaje de {1} tiros".format(jugador_mayor_tiros_campo, mayor_cantidad_tiros_campo))

#---------------------------------------------------------------------------------------------------

#9)

def jugador_mayor_asistencias(lista:list):

    jugador_mayor_asistencias = ""
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

    for jugador in lista:
        if jugador["estadisticas"]["promedio_puntos_por_partido"] > valor_ingresado:
            print(jugador["nombre"])

#---------------------------------------------------------------------------------------------------

#11)

def jugador_mas_rebotes_partido(lista:list):

    valor_ingresado = int(input("ingrese un valor: "))

    for jugador in lista:
        if jugador["estadisticas"]["promedio_rebotes_por_partido"] > valor_ingresado:
            print(jugador["nombre"])
            
#---------------------------------------------------------------------------------------------------

#12)

def jugador_mas_asistencias_partido(lista:list):

    valor_ingresado = int(input("ingrese un valor: "))

    for jugador in lista:
        if jugador["estadisticas"]["promedio_asistencias_por_partido"] > valor_ingresado:
            print(jugador["nombre"])


#---------------------------------------------------------------------------------------------------

#13)

def jugador_mayor_robos_totales(lista:list):

    jugador_mayor_robos_totales = ""
    mayor_cantidad_robos = 0

    for jugador in lista:
        if jugador["estadisticas"]["robos_totales"] > mayor_cantidad_robos:
            jugador_mayor_robos_totales = jugador["nombre"]
            mayor_cantidad_robos = jugador["estadisticas"]["robos_totales"]

    return print("el jugador con mayor robos totales es {0} con una cantidad de {1} robos".format(jugador_mayor_robos_totales, mayor_cantidad_robos))

#-----------------------------------------------------------------------------------------------------

#14)

def jugador_mayor_bloqueos_totales(lista:list):

    jugador_mayor_bloqueos_totales = ""
    mayor_cantidad_bloqueos = 0

    for jugador in lista:
        if jugador["estadisticas"]["bloqueos_totales"] > mayor_cantidad_bloqueos:
           jugador_mayor_bloqueos_totales = jugador["nombre"]
           mayor_cantidad_bloqueos = jugador["estadisticas"]["bloqueos_totales"]

    return print("el jugador con mayor bloqueos totales es {0} con una cantidad de {1} bloqueos".format(jugador_mayor_bloqueos_totales, mayor_cantidad_bloqueos))

#----------------------------------------------------------------------------------------------------- 

#15)


def jugador_mayor_tiros_libres(lista:list):

    valor_ingresado = int(input("ingrese un valor: "))

    for jugador in lista:
        if jugador["estadisticas"]["porcentaje_tiros_libres"] > valor_ingresado:
            print(jugador["nombre"])


#------------------------------------------------------------------------------------------------------ 

#16)
"""
def promedio_puntos_partido_sin_puntaje_mas_bajo(lista:list):

    indice = 0
    cantidad_puntos = 0
    
    for jugador in lista:
        indice += 1
        puntos = jugador["estadisticas"]["promedio_puntos_por_partido"]
        cantidad_puntos += puntos
        jugador_puntos = print(indice, "{0}: {1}".format(jugador["nombre"], jugador["estadisticas"]["promedio_puntos_por_partido"]))
    
    promedio_total = cantidad_puntos / len(lista)

    return print("promedio: ", promedio_total)

promedio_puntos_partido_sin_puntaje_mas_bajo(lista_jugadores)

"""





"""
while True:
    # Mostrar menú de opciones
    print("Menú de opciones:")
    print("1. Agregar un nuevo miembro")
    print("2. Mostrar la informacion de todos los miembros")
    print("3. Actualizar el tipo de membresía de un miembro")
    print("4. Buscar información de un miembro")
    print("5. Calcular el promedio de edad de los miembros")
    print("6. Buscar el miembro más joven y el más viejo")
    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")


    # Opción 1: Agregar un nuevo miembro
    if opcion == "1":
        pass

    # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        print("Nro ID.\tNombre\tEdad\tTipo membresia")
       
    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        pass


    # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        pass


    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        pass


    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
        pass


    # Opcion 0: Salir
    elif opcion == "0":
        break


    else:
        print("Opción inválida. Intente de nuevo.")

"""


