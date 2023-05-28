import json
from parcial_biblioteca import *
path_file = "C:/Users/JulioBC/Documents/Archivos Universidad/1_cuatrimestre/laboratorio_programacion/parcial-1/dt.json"


with open(path_file, "r") as file:
    data = json.load(file)

data2 = [1, 2, 3]
# mostrar_nombre_jugadores(data['jugadores'])

mostrar_estadisticas_jugador(data['jugadores'])