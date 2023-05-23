"""
Pre: --
Post: El programa recoge de entrada un conjunto de tarea y su nivel de prioridad [prioridad] [tarea Nº] y luego
      se va ordenando según mayor prioridad tenga. cuanto mayor sea el primer numero mayor será su prioridad.
      se ordean de manera ascendente en prioridad y descendente en Nº de tarea.
"""
sc = input("cuántas tareas hay en la lista de felipe?: ")
while(sc != "0"):
    total_tareas = int(sc)
    lista = []
    for _ in range(total_tareas) :
        sc = input("[prioridad] [tarea]")
        datos = sc.split()
        if len(datos) >= 2:
            prioridad = int(datos[0])
            tarea = int(datos[1])
            lista.append([prioridad, tarea])
        else:
            print("Datos incompletos. Se omitirá esta tarea.")
    ordenar = sorted(lista, key=lambda x: (-int(x[0]), int(x[1])))
    for i in ordenar:
        print(i)
    print("----")
    print("")
    sc = input("cuántas tareas hay en la lista de felipe?: ")