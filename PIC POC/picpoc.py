"""
Este es el famoso juego (PIC POC). el programa recibe por consola el total de sonodos escuchados durante la partida,
finalemte imprime por pantalla los puntos de cada jugador, a la izquierda (PIC) y a la derecha (poc)
"""
sc = input("numero de sondos reproducidos: ")
numero = int(sc)
sc = input("inserte sondos[pic] [poc] separados por un espacio: ")
lista = sc.split()
pic = 0
poc = 0
last = ""
for i in lista:
    if i.lower() == "pic":
        last = i
    elif i.lower() == "poc":
        last = i
    if i.lower() == "pong" and last.lower() =="pic":
        pic += 1
        last = "poc"
    elif i.lower() == "pong" and last.lower() =="poc":
        poc += 1
        last = "pic"
print(f"{pic} {poc}")