#Escreva uma função recursiva que multiplica os elementos de uma lista de números

def multiplicar_lista(lista):
    # Caso base: Se a lista estiver vazia, o resultado é 1.
    if not lista:
        return 1
    else:
        # A função recursiva multiplica o primeiro elemento da lista
        # pelo resultado da chamada recursiva para o restante da lista.
        return lista[0] * multiplicar_lista(lista[1:])

# Exemplo de uso:
lista_de_numeros = [2, 3, 4, 5]
resultado = multiplicar_lista(lista_de_numeros)
print(f"O resultado da multiplicação é: {resultado}")
