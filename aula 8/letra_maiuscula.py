def strings_letra_maiuscula(lista):
    
    return list(filter(lambda s: s[0].isupper(), lista))

lista_cor = ["azul", "amarelo", "verde", "Vermelho", "Roxo", "Anil"]
print(strings_letra_maiuscula(lista_cor))