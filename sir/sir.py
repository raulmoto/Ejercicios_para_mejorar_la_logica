"""
    Pre: --
    Post: el programa funciona de la siguiente forma. se insert primero un autor y la fecha en la que fue nombrado sir,
          luego se nos pide insertar cuantos libros tiene publicados ese autor y la fecha en la que lo publicó. el rpograma
          analiza las lineas en busca del primer libro publicado despues de el nombramiento de sir, pueda que halla publicado
          varios libros pero buscamos el mas cercano a la fecha de nombramiento.
"""
sc = input("inserte la fecha de condecoracion y el nombre del autor separado por un espacio: ")
datos = sc.split()
fecha_referencia = int(datos[0])
#autor = " ".join(datos[1:len(datos)])
sc = input("inserte el total de obras: ")
numero = int(sc)
fechamayor = 0
fechamenor = 0
result = ""
for _ in range(numero):
    sc = input("inserte [fecha de publicacion] [titulo]: ")
    datos = sc.split()
    fechaPublicacion = int(datos[0])
    titulo = " " .join(datos[1:len(datos)])
    if _ == 0:
        if fechaPublicacion >= fecha_referencia:
            fechamayor = fechaPublicacion
            result = titulo
    else:
        if fechamayor != 0: 
            if fechaPublicacion < fechamayor and fechaPublicacion >= fecha_referencia:
                fechamayor = fechaPublicacion
                result = titulo
        else:
            if fechaPublicacion >= fecha_referencia:
                fechamayor = fechaPublicacion
                result = titulo

if len(result) != 0:
    print(result)
else:
    print("Ninguno")