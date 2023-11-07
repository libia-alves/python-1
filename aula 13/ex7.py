# Crie uma função que tente dividir dois números e trate o erro se um deles não for numérico

def dividir_numeros(a, b):
    try:
        numero1 = float(a)
        numero2 = float(b)
        
        resultado = numero1 / numero2
        return resultado
    except (ValueError, ZeroDivisionError):
        print("Erro: Um ou ambos os valores não são numéricos ou ocorreu uma divisão por zero.")
        return None

# Exemplo de uso:
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

resultado_divisao = dividir_numeros(numero1, numero2)

if resultado_divisao is not None:
    print(f"Resultado da divisão: {resultado_divisao}")
else:
    print("Erro ao dividir os números.")
