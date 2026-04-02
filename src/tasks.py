import database


def agregar_tareas(descripcion):
    nueva_tarea = {
        'Id' : len(database.tareas) + 1, 
        'Descripcion' : descripcion, 
        'Completado' : False,
        }
    database.tareas.append(nueva_tarea)
    database.guardar_datos(database.tareas)

def mostrar_tareas():
    for tarea in database.tareas:
        print(f'ID: {tarea['Id']} - Descripcion: {tarea['Descripcion']} - Estado: {tarea['Completado']}')

def completar_tarea(id_buscar):
    for tarea in database.tareas:
        if id_buscar == tarea['Id']:
            tarea['Completado'] = True
    database.guardar_datos(database.tareas)


def eliminar_tarea(id_borrar):
    for tarea in database.tareas:
        if id_borrar == tarea['Id'] and tarea['Completado'] == True:
            database.tareas.remove(tarea)
    database.guardar_datos(database.tareas)            