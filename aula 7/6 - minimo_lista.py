#Escreva uma função recursiva que encontra o mínimo de uma lista de números.

def encontrar_minimo(lista):
    # Caso base: Se a lista estiver vazia, não há mínimo a ser encontrado.
    if not lista:
        return None
    elif len(lista) == 1:
        return lista[0]
    else:
        # Encontra o mínimo entre o primeiro elemento e o mínimo do restante da lista.
        min_resto = encontrar_minimo(lista[1:])
        return lista[0] if lista[0] < min_resto else min_resto

# Exemplo de uso:
lista_de_numeros = [5, 2, 9, 1, 7, 3]
minimo = encontrar_minimo(lista_de_numeros)
print(f"O valor mínimo na lista é: {minimo}")
