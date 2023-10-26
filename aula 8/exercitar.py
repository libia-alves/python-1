#Escreva uma função que recebe uma lista de números e retorna uma nova lista com 
#o dobro dos elementos.

def dobro_elementos(lista):
    dobro = lambda x: x * 2
    return list(map(lambda x: x * 2, lista))
lista_int = [1,1,1,2,2,2,5,5,5,3,3,3,5,5,5,8,8,8,7,7,7]
print(dobro_elementos(lista_int))




#mostrar os numeros pares

def numeros_pares(lista):
    
    return list(filter(lambda x: x % 2 == 0, lista))
lista_int = [1,1,1,2,2,2,5,5,5,3,3,3,5,5,5,8,8,8,7,7,7]
print(numeros_pares(lista_int))





from functools import reduce

def soma_elementos(lista):
    
    return reduce(lambda x, y: x + y, lista)
lista_int = [1,1,1,2,2,2,3,3,3,5,5,5,8,8,8,7,7,7,15,12,13,25,100]
print(soma_elementos(lista_int))




from functools import reduce 

def concantenar_strings(lista):
    
    return reduce(lambda x, y: x + y, lista)


lista_cor = ["azul", "amarelo", "verde", "vermelho", "roxo", "anil" ]
print(concantenar_strings(lista_cor))
concantenado = concantenar_strings(lista_cor)
print((concantenado[0:3]))
print((concantenado[4:11]))
print((concantenado[11:16]))