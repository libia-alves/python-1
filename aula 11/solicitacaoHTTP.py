# . Atividade 1: Escreva um programa que faça uma solicitação HTTP a uma URL e exiba o
#status da resposta (código de status) na tela.


import requests

# URL da qual você deseja obter o status
url = "https://www.example.com"  # Substitua pela URL desejada

# Fazer a solicitação HTTP
response = requests.get(url)

# Exibir o código de status
print(f"Status da resposta: {response.status_code}")
