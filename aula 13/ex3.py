#  Crie uma função que receba uma lista e um índice, e retorne o elemento naquele índice.
# Trate o erro se o índice estiver fora dos limites da lista.


def obter_elemento_por_indice(lista, indice):
    try:
        elemento = lista[indice]
        return elemento
    except IndexError:
        print(f"Erro: O índice {indice} está fora dos limites da lista.")
        return None

# Exemplo de uso:
minha_lista = [10, 20, 30, 40, 50]

indice_desejado = int(input("Digite o índice desejado: "))

elemento = obter_elemento_por_indice(minha_lista, indice_desejado)

if elemento is not None:
    print(f"Elemento no índice {indice_desejado}: {elemento}")
else:
    print("Erro ao acessar o índice da lista.")
