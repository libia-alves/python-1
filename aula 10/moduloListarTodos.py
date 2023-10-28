#Crie uma função que liste todos os arquivos em um diretório usando o módulo `os`

    
import os

    
diretorio = r"C:\Users\libia\OneDrive\Área de Trabalho\ibi\cyberedux\python 1\python-1"

arquivos = os.listdir(diretorio)
    
print("Arquivos no diretorio:")

for arquivo in arquivos:
    print(arquivo)