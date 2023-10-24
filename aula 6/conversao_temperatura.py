# crie uma função chamada converte_temperatura que onverge umsa temperatura de graus celsius para fahrenheit. a formula da 
# conversão é: Fahrenheit = (Celsius * 9/5) + 32. Peça ao usuário para inserir a temperatura em graus Celsius e, em seguida, 
# chame a função converge_temperatura para realizar a conversão e exibir o resultado em Fahrenheit.



def converte_temperatura (c):
    f = (c *9/5) + 32  
    return f
    
    

c = float(input("Digite a temperatura em graus Celsius: "))
f = converte_temperatura(c)
print(f"Resultado: {f}")