import json

def cargar_datos():
    try:
        with open("src/tareas.json","r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

tareas = cargar_datos()

def guardar_datos(lista_tareas):
    with open("src/tareas.json", "w") as archivo:
        json.dump(lista_tareas, archivo, indent=4)

