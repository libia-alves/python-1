# Crie uma função que receba dois números e tente calcular a raiz quadrada da soma deles.
# Trate o erro se a soma for zero. 

import math

def calcular_raiz_soma(numero1, numero2):
    try:
        soma = numero1 + numero2
        if soma < 0:
            raise ValueError("A soma é negativa, não é possível calcular a raiz quadrada.")
        
        raiz_soma = math.sqrt(soma)
        return raiz_soma
    except ValueError as e:
        print(f"Erro: {e}")
        return None

# Exemplo de uso:
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

raiz_soma = calcular_raiz_soma(numero1, numero2)

if raiz_soma is not None:
    print(f"Raiz quadrada da soma: {raiz_soma}")
else:
    print("Erro ao calcular a raiz quadrada da soma.")