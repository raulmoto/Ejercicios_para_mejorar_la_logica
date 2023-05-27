"""
El programa recibe por consola un primer valor numerico que indica el total de casos a analizar.
Seguido, el programa nos pedirá que se inserte cuantas amigos han quedado con Susanita (n) y 
cuanto es el salto que hacen para poder escabullirse (m)
"""
sc = input("inserta el numero de casos a analizar: ")
casos = int (sc)
posiciones = []
posiciones_original = []
for _ in range(casos):
    sc = input("inserta [total amigos] [saltos]: ")
    datos = sc.split()
    amigos = int(datos[0])
    saltos = int(datos[1])
    lista = ["amigo"] * amigos
    for i in range(len(lista)):
        posiciones_original.append(i+1)
    for i in range(1,len(lista),saltos):
        if (len(posiciones) < len(lista)) and i not in posiciones:
            posiciones.append(i)
        if i == len(lista) and len(posiciones)+1 < len(lista):
            i = (i +1) % len(lista)
    resto = set(posiciones_original) - set(posiciones)
    print(resto)