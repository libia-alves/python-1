# Crie uma função que tente abrir um arquivo e trate o erro se o arquivo não existir

def abrir_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
        return conteudo
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None

# Exemplo de uso:
nome_do_arquivo = input("Digite o nome do arquivo que deseja abrir: ")

conteudo_arquivo = abrir_arquivo(nome_do_arquivo)

if conteudo_arquivo is not None:
    print(f"Conteúdo do arquivo '{nome_do_arquivo}':\n{conteudo_arquivo}")
else:
    print("Erro ao abrir o arquivo.")
