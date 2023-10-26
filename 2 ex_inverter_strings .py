def inverter_strings(lista):
    return list(map(lambda s: s[::-1], lista))

lista_cor = ["azul", "amarelo", "verde", "vermelho", "roxo", "anil"]
print(inverter_strings(lista_cor))
#print(lista_cor.reverse())
print(lista_cor[0][0:2])