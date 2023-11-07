# Crie uma função que tente converter uma string em um número decimal e trate o erro se a
# conversão falhar.

def converter_para_decimal(string):
    try:
        numero_decimal = float(string)
        return numero_decimal
    except ValueError:
        print(f"Erro: Não foi possível converter '{string}' em um número decimal.")
        return None

# Exemplo de uso:
entrada = input("Digite um número decimal: ")
resultado = converter_para_decimal(entrada)

if resultado is not None:
    print(f"Você digitou o número decimal: {resultado}")
else:
    print("Conversão falhou.")