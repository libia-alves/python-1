
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

numero = int(input("Informe um numero para calcular seu faotorial: "))
print(f"O fatorial de {numero} é {fatorial(numero)}. ")