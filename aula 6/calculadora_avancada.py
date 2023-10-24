

def calculadora_avancada(a, b, operacao, op_avancada=None):
    if operacao == "basica":
        if op_avancada == "+":
            return a + b
        elif op_avancada == "-":
            return a - b
        elif op_avancada == "*":
            return a * b
        elif op_avancada == "/":
            return a / b 
    if operacao == "avançada":
        if op_avancada == "potenciacao":
              return a ** b
        elif op_avancada == "radiciação":
              return a ** (1/b)
        return "Operação Inválida"
          
            
a = float(input("Digite o primeiro numero: "))
b = float(input("Digite o segundo numero: "))
operacao = input("Escolha a operação (basica ou avançada): ")
op_avancada = input("Escolhaa operação avançada (potenciacao ou raiz): ")
resultado = calculadora_avancada(a, b, operacao, op_avancada)

print(f"Resultado: {resultado}")


