
def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista [0] + soma_lista(lista[1:])
lista = [20,30,40,50,60,70,90,100,1111,9999]
print(soma_lista(lista))


def media_lista(lista):
    if len (lista) == 0:
        return 0
    else:
        return soma_lista(lista) / len(lista)
    
mlista = [10,10,10]
print(media_lista(mlista))