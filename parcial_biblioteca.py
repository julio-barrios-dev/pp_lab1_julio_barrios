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

