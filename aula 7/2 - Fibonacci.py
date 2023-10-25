# Escreva uma função recursiva que calcula o número de Fibonacci de um número.

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
numero = int(input("Informe um número para saber qual é na sequencia de Fibonacci: "))
print(f"O número {numero} na sequencia de Fibonacci é {fibonacci(numero)}")