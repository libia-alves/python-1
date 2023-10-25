registro_conversoes = {}

def converte_temperatura_com_registro():
    while True:
        temperatura_celsius = float(input("Digite a temperatura em graus Celsius"))
        temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
        registro_conversoes[temperatura_celsius] = temperatura_fahrenheit
        print(f"A temperatura em graus Fahrenheit é: {temperatura_fahrenheit}")
        
        continuar = input("Deseja realizar outra conversão? (S para sim, N para não)")
        if continuar.upper() != 'S':
            break
        
    mostrar_registro = input("Deseja ver o registro das conversões? (S para sim N para não) ")
    if mostrar_registro.upper() == 'S':
        print("\nRegistro das Conversões: ")
        for celsius, fahrenheit in registro_conversoes.items():
               print(f"{celsius} C => {fahrenheit} F")
            
     
        
converte_temperatura_com_registro()
