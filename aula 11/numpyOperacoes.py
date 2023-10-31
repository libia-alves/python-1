#2. Atividade 2: Crie dois arrays NumPy com números inteiros e realize operações de adição,
#subtração, multiplicação e divisão elementar entre eles.


import numpy as np

# Criar dois arrays NumPy com números inteiros
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])

# Realizar operações elementares
soma = array1 + array2
subtracao = array1 - array2
multiplicacao = array1 * array2
divisao = array1 / array2

# Imprimir os resultados
print("Array 1:", array1)
print("Array 2:", array2)
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
