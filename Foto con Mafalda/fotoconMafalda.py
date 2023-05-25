"""
   Programa: Foto con Mafalda.
   El programa recibe como primera entrada el numero (n) de personas que quieren tomarse la foto en el mural de personajes.
   luego nos pide insertar los nombres de los personajes.
   Mafalda es el personaje fundamental, sin ella no se toma la foto. Para que se pueda tomar una foto, tiene que haber alguien
   (algun fanatico) en el puesto de Mafalda y dos personajes mas.
   se imprime por pantalla la cantidad de fotos tomadas en total y la cantidad de personajes del mural que nadie eligio para 
   tomarse la foto.
"""
sc = input("cuantas personas se tomarán la foto?: ")
total_peronas = int(sc)
lista = []
total_fanaticos = 0
totalFoto = 0
contador = 0
vecesMafalda = 0
nombres = []
listaPersonajes = ["Mafalda","Felipe","Manolito","Susanita","Miguelito","Libertad","Guille"]
personajesUsados = []
Mafalda = []
if 1 <= total_peronas and total_peronas <= 200000:
    print("hola!, en el mural de presonajes tenemos a:\nMafalda, \nFelipe, \nManolito, \nSusanita, \nMiguelito, \nLibertad o Guille)")
    print("")
    for i in range(total_peronas):
        sc = input(f"escribe el {i+1}er peronaje: ")
        lista.append(sc)

    iterador = 0    
    while(iterador < len(lista)):
        print(f"-->>>{lista[iterador]}" )
        if lista[iterador] == "Mafalda" and vecesMafalda < 1:
            if i not in nombres:
                total_fanaticos += 1
                nombres.append(lista[iterador])
                vecesMafalda += 1
        elif lista[iterador]  != "Mafalda" and  total_fanaticos < 4 and contador != 2 and lista[iterador] not in personajesUsados:
            if lista[iterador] not in nombres and contador != 2:
                total_fanaticos += 1
                nombres.append(lista[iterador])
                contador += 1
        if total_fanaticos < 4 and "Mafalda" in nombres and contador == 2:
            totalFoto += 1
            vecesMafalda = 0
            contador = 0
            iterador = 0
            total_fanaticos = 0
            copia_nombres = nombres.copy()
            for i in copia_nombres:
                if i not in personajesUsados:
                    personajesUsados.append(i)
                    lista.remove(i)
                    nombres.remove(i)
                else:
                    lista.remove(i)
                    nombres.remove(i)
        if "Mafalda" not in lista:
            personajesFaltantes = set(lista) - set(personajesUsados)
            cantidadFaltante = len(personajesFaltantes)
            break
        else:
            iterador = (iterador + 1) % len(lista)
    print(f"{totalFoto} {cantidadFaltante}")
else:
    print("total personas incorrecto, debe ser mayor a 1 y menor a 200.000")