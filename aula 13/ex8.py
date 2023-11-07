# Crie uma função que receba uma lista e um índice, e tente acessar o elemento naquele
#índice. Trate o erro se o índice não for um número inteiro.

def acessar_elemento_lista(lista, indice):
    try:
        indice = int(indice)  # Tentar converter o índice para um número inteiro
        elemento = lista[indice]  # Tentar acessar o elemento na lista
        return elemento
    except (ValueError, TypeError):
        print(f"Erro: O índice '{indice}' não é um número inteiro.")
        return None
    except IndexError:
        print(f"Erro: O índice '{indice}' está fora dos limites da lista.")
        return None

# Exemplo de uso:
minha_lista = [10, 20, 30, 40, 50]

indice_desejado = input("Digite o índice desejado: ")

elemento = acessar_elemento_lista(minha_lista, indice_desejado)

if elemento is not None:
    print(f"Elemento no índice {indice_desejado}: {elemento}")
else:
    print("Erro ao acessar o índice da lista.")
