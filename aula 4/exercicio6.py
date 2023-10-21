# Dada uma lista de numeros, crie um dicionario onde as chaves 'nome', 'preco' e ' quantidade_em_estoque


nomes = ['Produto A', 'Produto B', 'Produto C']
precos = [10.99, 19.95, 7.99]
quantidades_em_estoque = [50, 30, 100]

# Criando um dicionário a partir das três listas
produtos = []

for i in range(len(nomes)):
    produto = {
        'nome': nomes[i],
        'preco': precos[i],
        'quantidade_em_estoque': quantidades_em_estoque[i]
    }
    produtos.append(produto)

