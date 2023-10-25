def inverter_string(s):
    if len(s) == 0:
        return s
    else:
        return inverter_string(s[1:]) + s[0]
    
palavra = input("Informe uma palavra: ")
print(f"A palavra {palavra} foi invertida {inverter_string(palavra)}:")