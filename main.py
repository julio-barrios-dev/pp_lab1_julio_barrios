import json
from parcial_biblioteca import *
path_file = "C:/Users/JulioBC/Documents/Archivos Universidad/1_cuatrimestre/laboratorio_programacion/parcial-1/dt.json"


with open(path_file, "r") as file:
    data = json.load(file)

data2 = [1, 2, 3, 0, -5, -7]
# mostrar_nombre_jugadores(data['jugadores'])

# mostrar_estadisticas_jugador(data['jugadores'])

# buscar_jugador(data['jugadores'])

# promedio_puntos_partido(data['jugadores'])

# jugador_miembro_salon_baloncesto(data['jugadores'])
# jugador_mas_rebotes(data['jugadores'])
# jugador_mayor_tiros_campo(data['jugadores'])
# jugador_mayor_asistencias_totales(data['jugadores'])

jugadores_mayores_puntos_dato_usr(data['jugadores'])
