# 1. Atividade 1: Crie um gráfico de barras simples representando a contagem de votos para
#diferentes candidatos em uma eleição fictícia.  usando o Matplotlib


import matplotlib.pyplot as plt

# Dados fictícios dos candidatos e contagem de votos
candidatos = ['Candidato A', 'Candidato B', 'Candidato C', 'Candidato D']
votos = [350, 220, 180, 120]

# Criar o gráfico de barras
plt.bar(candidatos, votos, color='skyblue')

# Adicionar rótulos aos eixos
plt.xlabel('Candidatos')
plt.ylabel('Contagem de Votos')

# Adicionar um título ao gráfico
plt.title('Contagem de Votos por Candidato')

# Exibir o gráfico
plt.show()
