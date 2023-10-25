
def encontrar_maximo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        max_sublista = encontrar_maximo(lista[1:])
        return lista [0] if lista[0] > max_sublista else max_sublista
    
lista = [20,30,40,50,70,90,100]
print(encontrar_maximo(lista))