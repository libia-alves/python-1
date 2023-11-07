# Crie uma função que receba um número e tente calcular o logaritmo natural dele. Trate o
# erro se o número for negativo.


import math

def calcular_logaritmo_natural(numero):
    try:
        if numero <= 0:
            raise ValueError("O número deve ser positivo para calcular o logaritmo natural.")
        
        resultado = math.log(numero)
        return resultado
    except ValueError as e:
        print(f"Erro: {e}")
        return None

# Exemplo de uso:
numero = float(input("Digite um número positivo para calcular o logaritmo natural: "))

logaritmo = calcular_logaritmo_natural(numero)

if logaritmo is not None:
    print(f"Logaritmo natural de {numero}: {logaritmo}")
else:
    print("Erro ao calcular o logaritmo natural.")