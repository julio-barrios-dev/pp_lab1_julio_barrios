import json
from parcial_biblioteca import *
path_file = "C:/Users/JulioBC/Documents/Archivos Universidad/1_cuatrimestre/laboratorio_programacion/parcial-1/dt.json"


with open(path_file, "r") as file:
    data = json.load(file)

jugadores = data['jugadores']



funcion_principal(jugadores)