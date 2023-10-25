def calcular_media(lista):
    if not lista:
        return 0  # Se a lista estiver vazia, a média é 0 (caso base).
    else:
        primeiro_elemento = lista[0]
        soma_resto = calcular_media(lista[1:])
        return (primeiro_elemento + soma_resto) / len(lista)

# Exemplo de uso:
lista_de_numeros = [5, 2, 9, 1, 7, 3]
media = calcular_media(lista_de_numeros)
print(f"A média dos elementos na lista é: {media:.2f}")
