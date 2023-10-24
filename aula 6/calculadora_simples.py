#crie uma função chamada calculadora que recebe dois numeros e um operador como entrada. A função deve realizar 
# a operação correspondente (adição, subtração, multiplicação ou divisçao) com base no operador fornecido e retornar o resultado. 
#peça ao usuario para fornecer os numeros e o operador, chame a funçao e exiuba o resultado.



def calculadora(a, b, operador):
    if operador == '+':
        return a + b
    elif operador == '-':
        return a - b
    elif operador == '*':
        return a * b
    elif operador == '/':
        return a / b
  
    
a = float(input("Digite o primeiro numero: "))
b = float(input("Digite o segundo numero: "))


operador = input("Digite o operador ( + , - , * , / )")
resultado = calculadora(a, b, operador)
print(f"Resultado: {resultado}")





'''
outra forma de fazer:


def calculadora(a , b , operacao):
    if operacao == "+":
        return a + b
    elif operador == '-':
        return a - b
    elif operador == '*':
        return a * b
    elif operador == '/':
        return a / b
    
numero1 = float(input("Digite um numero:"))

numero2 = float(input("Digite outro numero:"))

operador = input("Digite um numero:")

resultado = calculadora(numero1, numero2, operador)
print(resultado)
'''