# Crie uma função que divide dois números e trate o erro se o divisor for zero.


def dividir (a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Erro: Divisão por zero nao é permitida")
        return None
    
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

resultado_divisao = dividir(numero1, numero2)

if resultado_divisao is not None:
    print(f"Resultado da divisão: {resultado_divisao}")
else:
    print("Divisão por zero não é permitida.")