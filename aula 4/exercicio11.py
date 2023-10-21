#Dada uma lista de palavras, crie um dicionário onde as chaves são as letras do alfabeto e
#os valores são listas de palavras que começam com essa letra


# Suponha que você tem uma lista de palavras
palavras = ['maçã', 'banana', 'abacaxi', 'laranja', 'pera', 'uva']

# Crie um dicionário vazio
dicionario_letras = {}

# Preencha o dicionário com as palavras
for palavra in palavras:
    primeira_letra = palavra[0].lower()  # Obtenha a primeira letra em minúsculas
    if primeira_letra.isalpha():  # Verifique se é uma letra do alfabeto
        if primeira_letra not in dicionario_letras:
            dicionario_letras[primeira_letra] = []
        dicionario_letras[primeira_letra].append(palavra)

# Agora, 'dicionario_letras' contém as letras do alfabeto como chaves e listas de palavras que começam com essas letras como valores
