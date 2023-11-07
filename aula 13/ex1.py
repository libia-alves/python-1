#Crie uma função que tente converter uma string em um número inteiro e trate o erro se a
#conversão 



def converter_para_inteiro(string):
    try:
        numero_inteiro = int(string)
        return numero_inteiro
    except ValueError:
        print(f"Erro: '{string}' não é um número inteiro válido.")
        return None


entrada = input("Digite um número inteiro: ")
resultado = converter_para_inteiro(entrada)

if resultado is not None:
    print(f"Você digitou o número inteiro: {resultado}")
else:
    print("Conversão falhou.")
