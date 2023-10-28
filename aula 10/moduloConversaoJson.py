#Converta um dicionário para uma string JSON usando o módulo `json`.


import json


dicionario = {"nome": "Libia", "idade": 19}


string_json = json.dumps(dicionario)

print("Diconario em Json:")
print(string_json)