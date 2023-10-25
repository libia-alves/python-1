def contar_ocorrencias(lista, elemento):

    if not lista:
        return 0
    else:
 
        if lista[0] == elemento:
            return 1 + contar_ocorrencias(lista[1:], elemento)
        else:
            return contar_ocorrencias(lista[1:], elemento)

# Exemplo de uso:
lista_de_numeros = [5, 2, 9, 1, 7, 5, 3, 5]
elemento_procurado = 5
ocorrencias = contar_ocorrencias(lista_de_numeros, elemento_procurado)
print(f"O elemento {elemento_procurado} ocorre {ocorrencias} vezes na lista.")
