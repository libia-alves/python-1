# 2. Atividade 2: Crie um programa que faça uma solicitação HTTP a uma API pública que
#forneça dados meteorológicos e exiba a previsão do tempo atual.

import requests

# Substitua 'Sao Paulo' pela cidade da qual você deseja obter a previsão do tempo
cidade = 'Cuiabá'

# URL da API Weatherstack
url = f'https://weatherstack.com/'

# Fazer a solicitação HTTP
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    data = response.json()
    temperatura = data['current']['temperature']
    descricao = data['current']['weather_descriptions'][0]

    print(f"Previsão do tempo para {cidade}:")
    print(f"Temperatura: {temperatura}°C")
    print(f"Descrição: {descricao}")
else:
    print("Falha ao obter a previsão do tempo. Verifique a cidade fornecida.")
