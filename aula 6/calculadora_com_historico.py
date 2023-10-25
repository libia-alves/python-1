historico = []  # Lista para armazenar o histórico de operações

def calculadora_com_historico():
    global historico  # Para acessar a lista de histórico global

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    operacao = input("Escolha a operação (adição, subtração, multiplicação, divisão): ")

    if operacao == "adição":
        resultado = num1 + num2
    elif operacao == "subtração":
        resultado = num1 - num2
    elif operacao == "multiplicação":
        resultado = num1 * num2
    elif operacao == "divisão":
        if num2 == 0:
            print("Erro! Divisão por zero.")
            return
        resultado = num1 / num2
    else:
        print("Operação inválida. Escolha entre adição, subtração, multiplicação ou divisão.")
        return

    operacao_realizada = f"{num1} {operacao} {num2} = {resultado}"
    historico.append(operacao_realizada)

    print(f"O resultado da operação é: {resultado}")

def exibir_historico():
    print("Histórico de Operações:")
    for operacao in historico:
        print(operacao)

# Exemplo de uso
while True:
    print("\nMenu:")
    print("1. Realizar operação")
    print("2. Exibir histórico")
    print("3. Sair")
    
    escolha = int(input("Escolha uma opção (1/2/3): "))

    if escolha == 1:
        calculadora_com_historico()
    elif escolha == 2:
        exibir_historico()
    elif escolha == 3:
        break
    else:
        print("Escolha inválida. Escolha 1, 2 ou 3.")
