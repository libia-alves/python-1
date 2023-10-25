def converte_temperatura_avancada():
    temperatura = float(input("Digite a temperatura: "))
    escolha = int(input("Escolha a conversão (1 para Celsius para Fahrenheit, 2 para Fahrenheit para Celsius): "))

    if escolha == 1:
        temperatura_fahrenheit = (temperatura * 9/5) + 32
        print(f"A temperatura em graus Fahrenheit é: {temperatura_fahrenheit:.1f}")
    elif escolha == 2:
        temperatura_celsius = (temperatura - 32) * 5/9
        print(f"A temperatura em graus Celsius é: {temperatura_celsius:.1f}")
    else:
        print("Escolha inválida. Por favor, escolha 1 ou 2 para a conversão.")

# Chame a função para realizar a conversão
converte_temperatura_avancada()
