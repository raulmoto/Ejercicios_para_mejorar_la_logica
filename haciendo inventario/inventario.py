"""
Pre:--
Post: el programa recibe por consola nombre de productos que va encontrando Manolito en su almacen y segun si ya los habia 
      anotado se sumará la cantidad, en caso que no exista en su lista se agregará.
"""
sc = input("cuántos productos ha encontrado manolito?: ")
num = int(sc)
inventario = {}
sc = input("nombre producto (0 para terminar): ")
while(sc != "0"):
    if sc.lower() in inventario:
        inventario[sc.lower()] += 1
    else:
        inventario[sc.lower()] = 1
    sc = input("nombre producto: ")
print(len(inventario))