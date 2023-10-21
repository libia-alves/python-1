#Dada uma lista de nomes, crie um dicionário onde as chaves são os nomes e os valores
#indicam se o nome tem mais de 5 letras ou não


nomes = ['Ana', 'Carlos', 'Mariana', 'João', 'Pedro', 'Luisa']

# Crie um dicionário com os nomes como chaves e um valor booleano para indicar se o nome tem mais de 5 letras
nomes_com_mais_de_5_letras = {}

for nome in nomes:
    tem_mais_de_5_letras = len(nome) > 5
    nomes_com_mais_de_5_letras[nome] = tem_mais_de_5_letras

# O dicionário 'nomes_com_mais_de_5_letras' terá as chaves como nomes e os valores como True ou False, dependendo se o nome tem mais de 5 letras ou não
