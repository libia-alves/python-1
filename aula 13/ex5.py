# Crie uma função que receba uma string e tente convertê-la para maiúsculas. Trate o erro se
# a entrada não for uma string

def converter_para_maiusculas(texto):
    try:
        if not isinstance(texto, str):
            raise TypeError("Entrada não é uma string")
        
        texto_maiusculo = texto.upper()
        return texto_maiusculo
    except TypeError as e:
        print(f"Erro: {e}")
        return None

# Exemplo de uso:
entrada = input("Digite uma string para converter para maiúsculas: ")

texto_maiusculo = converter_para_maiusculas(entrada)

if texto_maiusculo is not None:
    print(f"String em maiúsculas: {texto_maiusculo}")
else:
    print("Erro ao converter a string para maiúsculas.")
