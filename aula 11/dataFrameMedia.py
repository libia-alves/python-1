#1. Atividade 1: Crie um DataFrame com informações de nomes, idades e cidades de
#algumas pessoas e, em seguida, calcule a média das idades


import pandas as pd

# Criar um dicionário com informações das pessoas
data = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Idade': [25, 32, 28, 41, 22],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Salvador', 'Brasília', 'Curitiba']
}

# Criar o DataFrame a partir do dicionário
df = pd.DataFrame(data)

# Calcular a média das idades
media_idades = df['Idade'].mean()

# Imprimir o DataFrame e a média das idades
print("DataFrame:")
print(df)
print("\nMédia das Idades:", media_idades)
