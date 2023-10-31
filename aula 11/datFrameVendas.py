# 1. Atividade 1: Crie um DataFrame com informações de nomes, idades e cidades de
#algumas pessoas e, em seguida, calcule a média das idades

import pandas as pd

# Criar um dicionário com dados fictícios de vendas
data = {
    'Produto': ['Produto A', 'Produto B', 'Produto A', 'Produto C', 'Produto B', 'Produto C'],
    'Quantidade': [5, 3, 2, 7, 4, 6],
    'Preço': [10.0, 15.0, 10.0, 8.0, 15.0, 12.0]
}

# Criar o DataFrame a partir do dicionário
df = pd.DataFrame(data)

# Calcular o total de vendas para cada produto
df['Total de Vendas'] = df['Quantidade'] * df['Preço']

# Imprimir o DataFrame com o total de vendas
print("DataFrame de Vendas:")
print(df)
