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

    promedios_puntos = {}
    for jugador in lista:
        promedio_puntos = jugador["estadisticas"]["promedio_puntos_por_partido"]
        promedios_puntos[jugador["nombre"]] = promedio_puntos

    
    claves = list(promedios_puntos.keys())

    cantidad_claves = len(claves)
    for i in range(cantidad_claves-1):
        for j in range(0, cantidad_claves-i-1):
            if promedios_puntos[claves[j]] > promedios_puntos[claves[j+1]]:
                claves[j], claves[j+1] = claves[j+1], claves[j]

    
    diccionario_ordenado = {}
    for clave in claves:
        diccionario_ordenado[clave] = promedios_puntos[clave]
    
    return print(diccionario_ordenado)


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

def promedio_puntos_partido_sin_puntaje_mas_bajo(lista:list):

    promedios_puntos = {}
    for jugador in lista:
        promedio_puntos = jugador["estadisticas"]["promedio_puntos_por_partido"]
        promedios_puntos[jugador["nombre"]] = promedio_puntos

    # Obtención del jugador con el menor puntaje de puntos
    jugador_menor_puntos = min(promedios_puntos, key=promedios_puntos.get)
    menor_puntos = promedios_puntos[jugador_menor_puntos]

    # Creación del nuevo diccionario sin el jugador con el menor puntaje de puntos
    diccionario_ordenado = {}
    for jugador, promedio_puntos in promedios_puntos.items():
        if promedio_puntos > menor_puntos:
            diccionario_ordenado[jugador] = promedio_puntos
    
    return print(diccionario_ordenado)


#-------------------------------------------------------------------------------------------------------

#17)

def jugador_mayor_logros(lista:list):

    max_logros = 0

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
    
    jugador_mayor_temporadas = ""
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
    
    valor_ingresado = int(input("ingrese un valor: "))
    
    if valor_ingresado > jugador["estadisticas"]["promedio_asistencias_por_partido"]:
            print(jugador["nombre"])

  


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


    # Opcion 0: Salir
    elif opcion == "0":
        break


    else:
        print("Opción inválida. Intente de nuevo.")




