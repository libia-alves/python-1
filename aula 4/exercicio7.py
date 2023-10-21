# Dada uma lista de notas, crie um dicionário onde as chaves são os nomes dos alunos e os
# valores são as médias correspondentes.

# Suponha que você tenha duas listas: uma com os nomes dos alunos e outra com as notas
nomes_alunos = ['Aluno1', 'Aluno2', 'Aluno3', 'Aluno4']
notas = [8.5, 7.2, 9.0, 6.8]  # Notas correspondentes aos alunos

# Crie um dicionário a partir das duas listas
medias_alunos = {}

for i in range(len(nomes_alunos)):
    aluno = nomes_alunos[i]
    nota = notas[i]
    medias_alunos[aluno] = nota

# Agora, 'medias_alunos' é um dicionário onde as chaves são os nomes dos alunos e os valores são as médias correspondentes
