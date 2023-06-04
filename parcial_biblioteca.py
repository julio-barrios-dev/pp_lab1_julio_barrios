import re
import os

def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')

def quick_sort(lista):
    """
    Esta es una implementación de Python del algoritmo quicksort para ordenar una lista de elementos.
    
    :param lista: una lista de elementos que deben ordenarse utilizando el algoritmo de clasificación rápida
    :return: La función `quick_sort` devuelve una lista ordenada en orden ascendente.
    """
    lista_izq = []
    lista_der = []

    if (len(lista) <= 1):
        return lista
    else:
        pivot = lista[0]
        for elemento in lista[1:]:
            if elemento > pivot:
                lista_der.append(elemento)
            else:
                lista_izq.append(elemento)
                
    lista_izq = quick_sort(lista_izq)
    lista_izq.append(pivot)
    lista_der = quick_sort(lista_der)
    lista_izq.extend(lista_der)

    return lista_izq

'''
1_ Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
Nombre Jugador - Posición. Ejemplo:
Michael Jordan - Escolta
'''
def mostrar_nombre_jugadores(lista_jugadores: list[dict]) ->None:
    """
    La función "mostrar_nombre_jugadores" toma una lista de diccionarios que contienen información del jugador
    e imprime el nombre y la posición de cada jugador.
    
    :param lista_jugadores: Una lista de diccionarios que contienen información sobre cada jugador, incluyendo
    su nombre y cargo
    :tipo lista_jugadores: lista[dict]
    """
    contador = 0
    if len(lista_jugadores) > 0:
        for jugador in lista_jugadores:
            contador+= 1
            print(f"{contador}_ {jugador['nombre']} - {jugador['posicion']}")
    else:
        print("La lista esta vacia")

    clear_console()

'''
2_ Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas completas, 
incluyendo temporadas jugadas, puntos totales, promedio de puntos por partido, rebotes totales, 
promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, 
robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros 
libres y porcentaje de tiros triples.
'''
def mostrar_estadisticas_jugador(lista_jugadores: list[dict]) ->None:
    """
    Esta función solicita al usuario que ingrese el índice de un jugador y muestra sus estadísticas desde un
    lista de jugadores.
    
    :param lista_jugadores: Una lista de diccionarios que contienen información sobre cada jugador, incluyendo
    su nombre y estadísticas
    :tipo lista_jugadores: lista[dict]
    """

    while True:
        jugador = input("Ingrese el indice del jugador (1-12): ")

        if jugador.isdigit():
            jugador = int(jugador)

            if jugador > 0 and jugador < 13:
                datos_jugador = lista_jugadores[jugador - 1]
                nombre = datos_jugador['nombre']
                mensaje = f"Jugador: {nombre} \n"
                estadisticas = datos_jugador['estadisticas']
                claves_csv = ['nombre']
                valores_cvs = [nombre]

                for estadistica in estadisticas:
                    valor = estadisticas[estadistica]
                    claves_csv.append(estadistica)
                    valores_cvs.append(str(valor))
                    mensaje += f"{estadistica}: {valor} \n"
                
                print(mensaje)
                while True:
                    guardar = input("¿Desea guardar los datos en un 'CSV'?(s/n)")

                    if re.match(r"^[sn]$", guardar.lower()):
                        if guardar.lower() == "s":
                            guardadr_estadisticas_jugador(nombre, claves_csv, valores_cvs)
                            print("Archivo guardado")
                            clear_console()
                            break
                        elif  guardar.lower() == "n":
                            clear_console()
                            break
            break


'''
3_ Después de mostrar las estadísticas de un jugador seleccionado por el usuario, permite al usuario guardar las estadísticas de ese jugador en un archivo CSV. El archivo CSV debe contener los siguientes campos: nombre, posición, temporadas, puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.
'''

def guardadr_estadisticas_jugador(nombre: str, claves: list[str], valores:list[str]):
    """
    Esta función toma el nombre de un jugador, una lista de claves y una lista de valores, y los guarda como un CSV
    archivo con el nombre del jugador en minúsculas con espacios reemplazados por guiones.
    
    :param nombre: Una cadena que representa el nombre del jugador cuyas estadísticas se están guardando
    :type nombre: str
    :param claves: una lista de cadenas que representan las claves o nombres de columna para los datos que se guardarán en un
    archivo CSV
    :type claves: lista[str]
    :param valores: Una lista de valores que representan las estadísticas de un jugador. Estos valores serán
    escrito en un archivo CSV
    :tipo valores: lista
    """
    nombre = re.sub(" ", "-", nombre.lower())
    PATH = f"C:/Users/JulioBC/Documents/Archivos Universidad/1_cuatrimestre/laboratorio_programacion/parcial-1/{nombre}-estadisticas.csv"
    with open(PATH, 'w') as file:
        claves_csv = f"{','.join(claves)} \n"
        valores_csv = f"{','.join(valores)} \n"
        file.write(claves_csv)
        file.write(valores_csv)

'''
4_ Permitir al usuario buscar un jugador por su nombre y mostrar sus logros, como campeonatos de la NBA, participaciones en el All-Star y pertenencia al Salón de la Fama del Baloncesto, etc.
'''

def buscar_jugador_logros(lista_jugadores: list[dict]):
    """
    Esta función busca el nombre de un jugador en una lista de diccionarios e imprime sus logros
    si se encuentra.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores, donde cada diccionario contiene
    información sobre un jugador, como su nombre y logros
    :tipo lista_jugadores: lista[dict]
    :return: La función no tiene una declaración de retorno, por lo que devolverá Ninguno de forma predeterminada.
    """
        
    nombre = input("Ingrese el nombre del jugador: ").lower()

    logros = ""
    resultados = 0

    if not len(lista_jugadores) > 0:
        print("La lista esta vacia")
        clear_console()
        return
    
    for jugador in lista_jugadores:
        if nombre == jugador['nombre'].lower():
            resultados = 1
            logros = "\n".join(jugador['logros'])
            print(logros)
            break
    if resultados == 0:
        print("No se encontraron resultados")
    clear_console()

'''
5_Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente.
'''

def promedio_puntos_partido(lista:list[str]) ->None:
    """
    Esta función toma una lista de diccionarios que contienen información del jugador y calcula, imprime y ordena
    el promedio de puntos por juego para cada jugador.
    
    :param lista: El parámetro "lista" es una lista de diccionarios, donde cada diccionario representa un
    jugador y sus estadísticas. El diccionario contiene las claves "nombre" (nombre del jugador) y
    "estadisticas" (estadísticas del jugador), donde "estadisticas" es otro diccionario que contiene las
    :tipo lista: lista[str]
    :return: La función no devuelve nada, está imprimiendo un mensaje a la consola.
    """
    if not (len(lista) > 0):
        print("La lista esta vacia")
        clear_console()
        return

    datos = {}
    for jugador in lista:
        nombre = jugador['nombre']
        promedio_puntos_partido = jugador['estadisticas']['promedio_puntos_por_partido']
        datos[nombre] = promedio_puntos_partido
    nombres_ordenados = quick_sort(list(datos.keys()))
    mensaje = f'Puntos promedio por partido de cada jugador: \n'

    for jugador in nombres_ordenados:
        mensaje += f"{jugador}: {datos[jugador]} \n"
    print(mensaje)
    clear_console()

'''
6_ Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.
'''

def jugador_miembro_salon_baloncesto(lista_jugadores: list[dict]):
    """
    Esta función comprueba si un jugador de baloncesto determinado es miembro del Salón de la Fama y devuelve un
    mensaje indicando si lo son o no.
    
    :param lista_jugadores: Una lista de diccionarios que representan a jugadores de baloncesto, donde cada
    el diccionario contiene información sobre un jugador, como su nombre y logros
    :tipo lista_jugadores: lista[dict]
    :return: La función no tiene una declaración de retorno, por lo que devolverá Ninguno de forma predeterminada.
    """
    nombre = input("Ingrese el nombre del jugador: ").lower()

    resultados = 0

    if not len(lista_jugadores) > 0:
        print("La lista esta vacia")
        clear_console()
        return
    
    for jugador in lista_jugadores:
        if nombre == jugador['nombre'].lower():
            if jugador['logros'][-1] == "Miembro del Salon de la Fama del Baloncesto":

                resultados = 1
                print(f"{jugador['nombre']} es miembro del salon de la fama")
                break

            else:
                resultados = 1
                print(f"{jugador['nombre']} no es miembro del salon de la fama")
                break
    if resultados == 0:
        print("No se encontraron resultados")
    clear_console()

'''
7_ Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
'''

def jugador_maxima_estadistica(lista_jugadores: list[dict], estadistica: str):
    """
    Esta función toma una lista de diccionarios que representan jugadores y una estadística, y devuelve el
    nombre y valor del jugador con el valor más alto para esa estadística.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores y sus estadísticas
    :tipo lista_jugadores: lista[dict]
    :param estadistica: "estadistica" es un parámetro de cadena que representa la estadística específica que
    queremos encontrar el valor máximo para en la lista de jugadores. Se utiliza para acceder al valor de ese
    estadística para cada jugador en el bucle
    :type estadistica:str
    :return: La función no tiene declaración de retorno, solo imprime el nombre del jugador con
    el valor más alto para la estadística especificada.
    """

    if not len(lista_jugadores) > 0:
        print("La lista esta vacia")
        clear_console()
        return
    
    nombre = ""
    max_estadistica = 0

    for jugador in lista_jugadores:
        valor_estadistica = jugador['estadisticas'][estadistica]
        if valor_estadistica > max_estadistica:
            nombre = jugador['nombre']
            max_estadistica = valor_estadistica
    print(f'{nombre}: {max_estadistica}')


def jugador_mas_rebotes(lista_jugadores: list[dict]):
    """
    Esta función llama a otra función para encontrar al jugador con el total de rebotes más alto de una lista
    de jugadores
    
    :param lista_jugadores: Una lista de diccionarios donde cada diccionario representa un jugador y
    contiene información sobre sus estadísticas
    :tipo lista_jugadores: lista[dict]
    """

    jugador_maxima_estadistica(lista_jugadores, 'rebotes_totales')

'''
8_ Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.
'''

def jugador_mayor_tiros_campo(lista_jugadores: list[dict]):
    """
    Esta función llama a otra función para encontrar al jugador con el mayor porcentaje de tiros de campo en un
    lista de jugadores.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores de baloncesto y sus estadísticas.
    Cada diccionario contiene claves para el nombre del jugador, el equipo, la posición y varias estadísticas como
    puntos por partido, rebotes por partido y porcentaje de tiros de campo
    :tipo lista_jugadores: lista[dict]
    """

    jugador_maxima_estadistica(lista_jugadores, 'porcentaje_tiros_de_campo')

'''
9_ Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.
'''

def jugador_mayor_asistencias_totales(lista_jugadores: list[dict]):
    """
    Esta función toma una lista de diccionarios que representan a jugadores de baloncesto y devuelve el jugador
    con el mayor número total de asistencias.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores de baloncesto y sus estadísticas.
    Cada diccionario contiene claves para el nombre del jugador, el equipo y varias estadísticas como puntos,
    rebotes y asistencias
    :tipo lista_jugadores: lista[dict]
    """

    jugador_maxima_estadistica(lista_jugadores, 'asistencias_totales')

'''
10_ Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.
'''

def jugadores_valores_mayores_segun_dato_usr(lista_jugadores: list[dict], estadistica: str):
    """
    Esta función toma una lista de diccionarios que representan a los jugadores y una estadística, solicita al usuario
    por un valor, y devuelve un mensaje con los nombres y valores de los jugadores cuya estadística es mayor
    que la entrada del usuario.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores y sus estadísticas
    :tipo lista_jugadores: lista[dict]
    :param estadistica: El parámetro "estadistica" es una cadena que representa la estadística o
    atributo de los jugadores que se utilizará para comparar sus valores y determinar cuáles tienen un
    valor superior al introducido por el usuario. Ejemplos de posibles valores para "estadistica" podrían
    ser "puntos", "
    :type estadistica:str
    :return: La función no tiene una declaración de devolución, por lo que devuelve Ninguno de forma predeterminada.
    """
    if not len(lista_jugadores) > 0:
        print("La lista esta vacia")
        clear_console()
        return
    
    while True:
        valor_usr = input("Ingresa un valor: ")
        if valor_usr.isdigit():
            valor_usr = int(valor_usr)
            break

    jugadores_mayor_valores = {}

    for jugador in lista_jugadores:
        nombre = jugador['nombre']
        valor_jugador = jugador['estadisticas'][estadistica]
        if valor_jugador > valor_usr:
            jugadores_mayor_valores[nombre] = valor_jugador
    mensaje = 'Jugadores con mayor puntaje segun el ingresado \n'
    if jugadores_mayor_valores:
        for jugador, valores in jugadores_mayor_valores.items():
            mensaje += f'{jugador}: {valores} \n'
    else:
        mensaje += "No hay jugadores con valores mayor al ingresado"

    print(mensaje)
    clear_console()

def jugadores_mayores_puntos_promedio_partido_dato_usr(lista_jugadores: list[dict]):
    """
    Esta función llama a otra función para encontrar los jugadores con los valores más altos para un determinado
    estadística en una lista de diccionarios que representan a jugadores de baloncesto.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores de baloncesto y sus estadísticas.
    Cada diccionario contiene claves como "nombre" (nombre), "edad" (edad), "promedio_puntos_por_partido"
    (promedio de puntos por partido), etc.
    :tipo lista_jugadores: lista[dict]
    """

    jugadores_valores_mayores_segun_dato_usr(lista_jugadores, 'promedio_puntos_por_partido')

'''
11_ Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.
'''

def jugadores_mayores_puntos_promedio_rebote_dato_usr(lista_jugadores: list[dict]):
    """
    Esta función llama a otra función para encontrar los jugadores con el promedio de rebotes más alto por
    juego de una lista de jugadores proporcionada como un diccionario.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores de baloncesto y sus estadísticas.
    Cada diccionario contiene claves para "nombre" (nombre), "edad" (edad), "promedio_puntos_por_partido"
    (media de puntos por partido), y "promedio_rebotes_por_partido" (media de rebotes por partido)
    :tipo lista_jugadores: lista[dict]
    """
    

    jugadores_valores_mayores_segun_dato_usr(lista_jugadores, 'promedio_rebotes_por_partido')

'''
12_ Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.
'''

def jugadores_mayores_asistencia_promedio_dato_usr(lista_jugadores: list[dict]):
    """
    Esta función llama a otra función para encontrar los jugadores con los valores más altos para un determinado
    estadística (en este caso, promedio de asistencias por partido) en una lista de diccionarios que representan el baloncesto
    jugadores
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores y sus estadísticas. Cada
    diccionario debe tener las siguientes claves: 'nombre' (cadena), 'edad' (entero), 'equipo' (cadena),
    'promedio_puntos_por_partido' (float), 'promedio_rebotes_por_partido' (
    :tipo lista_jugadores: lista[dict]
    """

    jugadores_valores_mayores_segun_dato_usr(lista_jugadores, 'promedio_asistencias_por_partido')

'''
13_ Calcular y mostrar el jugador con la mayor cantidad de robos totales.
'''

def jugador_mayor_robos_totales(lista_jugadores: list[dict]):
    """
    Esta función toma una lista de diccionarios que representan a jugadores de baloncesto y devuelve el jugador
    con los robos totales más altos.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores de baloncesto y sus estadísticas.
    Cada diccionario contiene claves para el nombre del jugador, el equipo, los juegos jugados, los robos por juego y el total
    roba
    :tipo lista_jugadores: lista[dict]
    """

    jugador_maxima_estadistica(lista_jugadores, 'robos_totales')

'''
14_ Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.
'''

def jugador_mayor_bloqueos_totales(lista_jugadores: list[dict]):
    """
    Esta función toma una lista de diccionarios que representan jugadores y devuelve el jugador con el
    estadística de bloques totales más alta.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores de baloncesto y sus estadísticas.
    Cada diccionario contiene claves para el nombre del jugador, el equipo, la posición y varias estadísticas como
    puntos, rebotes y tapones
    :tipo lista_jugadores: lista[dict]
    """


    jugador_maxima_estadistica(lista_jugadores, 'bloqueos_totales')

'''
15._  Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.
'''

def jugador_mayor_tiros_libres_dato_usr(lista_jugadores: list[dict]):
    """
    Esta función toma una lista de diccionarios que contienen información sobre jugadores de baloncesto y
    devuelve los jugadores con el mayor porcentaje de tiros libres según la entrada del usuario.
    
    :param lista_jugadores: Una lista de diccionarios donde cada diccionario representa un jugador y
    contiene información sobre su desempeño en un juego de baloncesto, incluido su nombre, equipo y
    estadísticas como puntos anotados, rebotes y porcentaje de tiros libres
    :tipo lista_jugadores: lista[dict]
    """

    jugadores_valores_mayores_segun_dato_usr(lista_jugadores, 'porcentaje_tiros_libres')

'''
16_ Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.
'''

def promedio_puntos_partido_menos_mas_bajo(lista_jugadores: list[dict]):
    """
    Esta función calcula el promedio de puntos por juego para cada jugador en una lista de diccionarios y
    devuelve los valores de todos los jugadores excepto el que tiene el promedio más bajo.
    
    :param lista_jugadores: Una lista de diccionarios que representan a los jugadores y sus estadísticas. Cada
    diccionario debe tener una tecla "nombre" con el nombre del jugador y una tecla "estadisticas" con un
    diccionario de estadísticas, incluyendo una tecla "promedio_puntos_por_partido" con la media del jugador
    puntos por juego
    :tipo lista_jugadores: lista[dict]
    :return: No se especifica lo que se devuelve. La función sólo imprime un mensaje al
    consola.
    """
      
    if not len(lista_jugadores) > 0:
        print("La lista esta vacia")
        clear_console()
        return
    
    min_valor = lista_jugadores[0]['estadisticas']['promedio_puntos_por_partido']
    nombre_min = ''

    for jugador in lista_jugadores:
        valor_estadistica = jugador['estadisticas']['promedio_puntos_por_partido']
        nombre = jugador['nombre']
        if valor_estadistica < min_valor:
            nombre_min = nombre
            min_valor = valor_estadistica

    mensaje = 'Promedio de puntos por partidos menos el mas bajo: \n'

    for jugador in lista_jugadores:
        if jugador["nombre"] == nombre_min:
            continue
        mensaje += f'{jugador["nombre"]}: {jugador["estadisticas"]["promedio_puntos_por_partido"]} \n'

    print(mensaje)
    clear_console()

'''
17_ Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos
'''
def jugador_mayor_logros(lista_jugadores: list[dict]):
    """
    Esta función toma una lista de diccionarios que representan a los jugadores y sus logros, y devuelve
    el nombre del jugador con más logros.
    
    :param lista_jugadores: El parámetro "lista_jugadores" es una lista de diccionarios, donde cada
    diccionario representa a un jugador y contiene información sobre su nombre y logros
    :tipo lista_jugadores: lista[dict]
    :return: La función no está devolviendo nada, está imprimiendo el nombre del jugador con el
    mayor número de logros y el número de logros que tienen.
    """

    if not len(lista_jugadores) > 0:
        print("La lista esta vacia")
        clear_console()
        return
    
    nombre = ""
    max_logros = 0

    for jugador in lista_jugadores:
        valor_logros = len(jugador['logros'])
        if valor_logros > max_logros:
            nombre = jugador['nombre']
            max_logros = valor_logros
    print(f'{nombre}: {max_logros}')

'''
18_ Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.
'''

def porcentaje_tiros_triples_mayor_dato_usr(lista_jugadores: list[dict]):
    """
    Esta función llama a otra función para encontrar los jugadores con los valores más altos para el
    Clave "porcentaje_tiros_triples" en una lista de diccionarios.
    
    :param lista_jugadores: Una lista de diccionarios donde cada diccionario representa un jugador y
    contiene información sobre su desempeño en un partido de baloncesto. El diccionario debe tener la
    siguientes claves: 'nombre' (string), 'puntos' (int), 'rebotes' (int), 'asistencias' (int), 'porcentaje
    :tipo lista_jugadores: lista[dict]
    """

    jugadores_valores_mayores_segun_dato_usr(lista_jugadores, 'porcentaje_tiros_triples')

'''
 19_ Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas
'''

def jugador_mayor_temporadas_jugadas(lista_jugadores: list[dict]):

    jugador_maxima_estadistica(lista_jugadores, 'temporadas')


'''
20_ Permitir al usuario ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.
'''

def mostrar_jugadores_posicion(lista_jugadores: list[dict]):

    if not len(lista_jugadores) > 0:
        print("La lista esta vacia")
        clear_console()
        return
    
    while True:
        valor_usr = input("Ingresa un valor: ")
        if valor_usr.isdigit():
            valor_usr = int(valor_usr)
            break

    jugadores_posiciones = []

    for jugador in lista_jugadores:
        jugadores_posiciones.append((jugador['nombre'], jugador['posicion'], jugador['estadisticas']['porcentaje_tiros_de_campo']))
    
    rango_jugadores = len(jugadores_posiciones)

    flag_swap = True
    while(flag_swap):
        flag_swap = False
        rango_jugadores = rango_jugadores - 1
        for jugador in range(rango_jugadores):

            if (jugadores_posiciones[jugador][1]) > (jugadores_posiciones[jugador + 1][1]):
                aux = jugadores_posiciones[jugador]
                jugadores_posiciones[jugador] = jugadores_posiciones[jugador + 1]
                jugadores_posiciones[jugador + 1] = aux
                flag_swap = True

    mensaje = f"Jugadores con porcentaje de tiros de campo superior al ingresado: \n"

    hay_jugadores = False

    for jugador in jugadores_posiciones:
        if jugador[2] > valor_usr:
            hay_jugadores = True
            mensaje += f"{jugador[0]}-{jugador[1]} -> {jugador[2]} \n"

    if hay_jugadores:
        print(mensaje)
    else:
        print("No hay jugadores con datos mayor al ingresado")

    clear_console()

'''
--------Parcial--------
'''
'''
1. Determinar la cantidad de jugadores que hay por cada posición.
Ejemplo:
Base: 2
Alero: 3
...
'''

def cantidad_jugadores_posicion(lista_jugadores: list[dict]):
    """
    Esta función toma una lista de diccionarios que representan a los jugadores y devuelve el recuento de jugadores para
    cada puesto
    
    :param lista_jugadores: Una lista de diccionarios que representan información sobre jugadores en un deporte
    equipo. Cada diccionario contiene claves de 'posición' y potencialmente otras claves con información sobre el
    jugador
    :tipo lista_jugadores: lista[dict]
    """
    posiciones = {}

    for jugador in lista_jugadores:
        if not jugador['posicion'] in posiciones:
            posiciones[jugador['posicion']] = 1
        else:
            posiciones[jugador['posicion']] += 1

    mensaje = "Cantidad de jugadores por pocision \n"

    for posicion,cantidad in posiciones.items():
        mensaje += f"{posicion}: {cantidad} \n"
    print(mensaje)

'''
2. Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente. 
La salida por pantalla debe tener un formato similar a este:
Michael Jordan (14 veces All Star)
Magic Johnson (12 veces All-Star)
...
'''
def jugadores_cantidad_all_star(lista_jugadores: list[dict]):
    """
    Esta función toma una lista de diccionarios que contienen información sobre los jugadores de baloncesto y sus
    logros y devuelve un mensaje que muestra el número de veces que cada jugador ha sido All-Star,
    ordenados de mayor a menor.
    
    :param lista_jugadores: El parámetro "lista_jugadores" es una lista de diccionarios, donde cada
    diccionario representa a un jugador y contiene información sobre su nombre y logros
    :tipo lista_jugadores: lista[dict]
    """
    jugadores_all_start = {}
    for jugador in lista_jugadores:
        jugadores_all_start[jugador['nombre']] = 0
        for logro in jugador['logros']:
            if re.search(r'All-Star$', logro):
                split_all_start = logro.split(' ')
                cantidad_all_start = split_all_start[0]
                jugadores_all_start[jugador['nombre']] = cantidad_all_start

    lista_all_start_jugadores = list(jugadores_all_start.items())
    rango_jugadores = len(lista_all_start_jugadores)
    flag_swap = True
    while(flag_swap):
        flag_swap = False
        rango_jugadores = rango_jugadores - 1
        for jugador in range(rango_jugadores):
            if int (lista_all_start_jugadores[jugador][1]) < int (lista_all_start_jugadores[jugador + 1][1]):
                aux = lista_all_start_jugadores[jugador]
                lista_all_start_jugadores[jugador] = lista_all_start_jugadores[jugador + 1]
                lista_all_start_jugadores[jugador + 1] = aux
    
    mensaje = "Cantidad de jugadores con mas a menor All Start \n"
    for jugador,cantidad in lista_all_start_jugadores:
        mensaje += f"{jugador}: {cantidad} veces All Star\n"
    print(mensaje)
    
'''
3_ Determinar qué jugador tiene las mejores estadísticas en cada valor. La salida por pantalla debe tener un formato similar a este:
Mayor cantidad de temporadas: Karl Malone (19)
Mayor cantidad de puntos totales: Karl Malon (36928)
'''

def jugadores_mejores_estadisticas(lista_jugadores: list[dict]):
    """
    Esta función toma una lista de diccionarios que contienen estadísticas de jugadores y devuelve el jugador con
    el valor más alto para cada categoría estadística.
    
    :param lista_jugadores: Una lista de diccionarios, donde cada diccionario representa un jugador y
    contiene su nombre y estadísticas
    :tipo lista_jugadores: lista[dict]
    """
    mejores_estadisticas_jugadores = {
        'temporadas': ['nombre', 0],
        'puntos_totales': ['nombre', 0],
        'promedio_puntos_por_partido': ['nombre', 0],
        'rebotes_totales': ['nombre', 0],
        'promedio_rebotes_por_partido': ['nombre', 0],
        'asistencias_totales': ['nombre', 0],
        'promedio_asistencias_por_partido': ['nombre', 0],
        'robos_totales': ['nombre', 0],
        'bloqueos_totales': ['nombre', 0],
        'porcentaje_tiros_de_campo': ['nombre', 0],
        'porcentaje_tiros_libres': ['nombre', 0],
        'porcentaje_tiros_triples': ['nombre', 0],
    }

    
    for estadistica in mejores_estadisticas_jugadores.keys():
        for jugador in lista_jugadores:
            estadisticas_jugador = jugador['estadisticas']
            if (estadisticas_jugador[estadistica]) > (mejores_estadisticas_jugadores[estadistica][1]):
               max_estadistica = estadisticas_jugador[estadistica]
               mejores_estadisticas_jugadores[estadistica] = [jugador['nombre'], max_estadistica]

    mensaje = "Jugadores con mejores estadisticas de cada valor: \n"

    for estadistica,dato in mejores_estadisticas_jugadores.items():
        mensaje += f"Mayor cantidad de {estadistica}: {dato[0]} {dato[1]} \n"
    print(mensaje)



def imprimir_menu() ->int:
    mensaje = '''
        Seleccione una opcion: 

        1._ Mostrar la lista de todos los jugadores del Dream Team

        2._ Seleccionar un jugador por su índice y mostrar sus estadísticas completas

        3._ Buscar un jugador por su nombre y mostrar sus logros.

        4._ Mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente. 

        5._ Ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.

        6._ Mostrar el jugador con la mayor cantidad de rebotes totales.

        7._ Mostrar el jugador con el mayor porcentaje de tiros de campo.

        8._ Mostrar el jugador con la mayor cantidad de asistencias totales.

        9._ Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.

        10._ Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.

        11._ Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.

        12._ Mostrar el jugador con la mayor cantidad de robos totales.

        13._ Mostrar el jugador con la mayor cantidad de bloqueos totales.

        14._ Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.

        15._ Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.

        16._ Mostrar el jugador con la mayor cantidad de logros obtenidos.

        17._ Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.

        18._ Mostrar el jugador con la mayor cantidad de temporadas jugadas

        19._ Ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.

        20._ Mostrar cantidad de jugadores que hay por posicion.

        21._ Mostrar cantidad de jugadores que hay por posicion.

        22._ Mostrar jugadores con mejores estadisticas de cada valor.
    '''

    print(mensaje)
    while True:
        dato = input('Ingrese un numero segun la lista: ')
        if dato.isdigit():
            dato = int(dato)
            if dato < 23 and dato > 0:
                return dato
def funcion_principal(jugadores: list[dict]):
    
    opcion =  imprimir_menu()

    match opcion:
        case 1: 
            mostrar_nombre_jugadores(jugadores)
        case 2: 
            mostrar_estadisticas_jugador(jugadores)
        case 3: 
            buscar_jugador_logros(jugadores)
        case 4: 
            promedio_puntos_partido(jugadores)
        case 5: 
            jugador_miembro_salon_baloncesto(jugadores)
        case 6: 
            jugador_mas_rebotes(jugadores)
        case 7: 
            jugador_mayor_tiros_campo(jugadores)
        case 8: 
            jugador_mayor_asistencias_totales(jugadores)
        case 9: 
            jugadores_mayores_puntos_promedio_partido_dato_usr(jugadores)
        case 10: 
            jugadores_mayores_puntos_promedio_rebote_dato_usr(jugadores)
        case 11: 
            jugadores_mayores_asistencia_promedio_dato_usr(jugadores)
        case 12: 
            jugador_mayor_robos_totales(jugadores)
        case 13: 
            jugador_mayor_bloqueos_totales(jugadores)
        case 14: 
            jugador_mayor_tiros_libres_dato_usr(jugadores)
        case 15: 
            promedio_puntos_partido_menos_mas_bajo(jugadores)
        case 16: 
            jugador_mayor_logros(jugadores)
        case 17: 
            porcentaje_tiros_triples_mayor_dato_usr(jugadores)
        case 18: 
            jugador_mayor_temporadas_jugadas(jugadores)
        case 19: 
            mostrar_jugadores_posicion(jugadores)
        case 20: 
            cantidad_jugadores_posicion(jugadores)
        case 21: 
            jugadores_cantidad_all_star(jugadores)
        case 22: 
            jugadores_mejores_estadisticas(jugadores)

    clear_console()