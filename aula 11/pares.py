# 1. Atividade 1: Crie um array NumPy contendo os números pares de 2 a 10 e, em seguida,
# calcule a média desses números

import numpy as np

# Criar um array NumPy com os números pares de 2 a 10
numeros_pares = np.array([2, 4, 6, 8, 10])

# Calcular a média dos números pares
media = np.mean(numeros_pares)

# Imprimir o array e a média
print("Array de números pares:", numeros_pares)
print("Média dos números pares:", media)
