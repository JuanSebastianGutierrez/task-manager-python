import tasks


while True:
    print('Menu de opciones Manejador de tareas: \n')
    print('1. Agregar tarea \n'
    '2. Mostrar tareas \n'
    '3. Completar tarea \n'
    '4. Eliminar tarea \n'
    '5. Salir \n'
    )


    print('Que opcion deseas: ')
    opcion = int(input())



    if opcion == 1:
        print('\n Elegiste agregar tarea \n')
        descripcion_usuario = input('Escribe la descripcion de la tarea que quieres realizar: ')
        tasks.agregar_tareas(descripcion_usuario)


    elif opcion == 2:
        print('\nElegiste mostrar las tareas \n')
        tasks.mostrar_tareas()


    elif opcion == 3:
        print('\n Elegiste finalizar una tarea')
        Id_completar = int(input('Digite el numero de la tarea quieres completar: '))
        tasks.completar_tarea(Id_completar)


    elif opcion == 4:
        print('\n Elegiste eliminar una tarea')
        print('Recuerde que la tarea tuvo que finalizar antes de realizar esta accion')
        Id_borrar = int(input('Digite el numero de la tarea que quiere eliminar: '))
        tasks.eliminar_tarea(Id_borrar)


    elif opcion == 5:
        print('\n Saliste del programa \n')
        break


    else:
        print('Opcion no valida')


