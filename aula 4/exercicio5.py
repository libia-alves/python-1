# Dada uma lista de números, crie um dicionário onde as chaves são os números e os valores
# indicam se o número é par ou ímpar


numeros = [1,2,3,4,5,6,7,8,9]
dic = {}

for i in numeros:
    if i % 2 == 0: 
        dic[i] = 'par'
    else:
        dic [i] = 'impar'
    
print (dic)