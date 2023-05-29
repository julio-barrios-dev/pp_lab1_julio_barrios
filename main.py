import json
from parcial_biblioteca import *
path_file = "C:/Users/JulioBC/Documents/Archivos Universidad/1_cuatrimestre/laboratorio_programacion/parcial-1/dt.json"


with open(path_file, "r") as file:
    data = json.load(file)

jugadores = data['jugadores']

def funcion_principal():
    
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
            print("No termine este punto ;C")

    clear_console()

funcion_principal()