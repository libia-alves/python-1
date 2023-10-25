#Escreva uma função recursiva que imprime os números de 1 a n.

def imprimir_numeros_ate_n(n):
    if n > 0:
        imprimir_numeros_ate_n(n - 1)  # Chama a função recursivamente para n-1
        print(n)

# Exemplo de uso:
n = 5
imprimir_numeros_ate_n(n)
