# Dado uma lista de palavras, crie um dicionario onde as chaves são as palavras e os valores são os números
#de vezes que cada palavra aparece na lista



palavras = ['banana', 'banana', 'maça', 'abacaxi', 'abacate']

dicionario = {}

for i in palavras:
    #print (i)
    
    if i in list(dicionario.keys()):
        dicionario[i] = dicionario[i] + 1
    else:
        dicionario[i] = 1    
        
print(dicionario)

