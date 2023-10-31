# 2. Atividade 2: Crie um gráfico de linha que mostre a evolução do preço de uma ação ao
#longo do tempo.
import matplotlib.pyplot as plt
from datetime import datetime

# Dados fictícios: datas e preços da ação
datas = ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']
precos_acao = [100, 105, 110, 108, 112]

# Converter as datas para o formato de data
datas = [datetime.strptime(date, "%Y-%m-%d") for date in datas]

# Criar o gráfico de linha
plt.plot(datas, precos_acao, marker='o', linestyle='-')

# Adicionar rótulos aos eixos
plt.xlabel('Data')
plt.ylabel('Preço da Ação')

# Adicionar um título ao gráfico
plt.title('Evolução do Preço da Ação ao Longo do Tempo')

# Rotacionar os rótulos do eixo x para melhor legibilidade
plt.xticks(rotation=45)

# Exibir o gráfico
plt.show()
