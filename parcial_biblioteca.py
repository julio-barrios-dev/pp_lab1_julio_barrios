import re
import os

def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')

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

def guardadr_estadisticas_jugador(nombre: str, claves: list[str], valores:list):
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