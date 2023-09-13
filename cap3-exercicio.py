# Análise de Dados
# Exercícios Propostos - Cap. 3

#1.
# Lista com os 5 primeiros colocados da Copa do Mundo 2022
campeoes = ['Argentina', 'França', 'Croácia', 'Marrocos', 'Holanda']

#a. Os 3 primeiros colocados
print(campeoes[0:3])

#b. Os 2 últimos colocados
print(campeoes[3:])

#c. Uma liusta com os times em ordem alfabética
print(sorted(campeoes)) #sorted pega uma lista e retorna uma nova lista com esses elementos na ordem ordenada

#d. Em que posição da tabela está Barcelona (mudei para França, pois não tem Barcelona)
posicao = campeoes.index('França') + 1 # pois a contagem começa em 0
print("A França está na posição:", posicao)

#2. 
# 
loja1 = {
    'Apple iPhone 13',
    'Apple iPhone 11',
    'Apple iPhone 12',
    'Samsung Galaxy s23'
}

loja2 = {
    'Samsung Galaxy s22',
    'Samsung Galaxy s23',
    'Samsung Galaxy s10+',
    'Samsung Galaxy s10',
    'Apple iPhone 12 pro'
}

print('Todos os modelos disponíveis: ', loja1.union(loja2))

print('Modelos disponíveis em ambas as lojas: ', loja1.intersection(loja2))

#3.
nome = str(input('Digite o nome do aluno: '))
media = float(input('Digite a média do aluno: '))

studentData = {}

studentData['nome'] = nome
studentData['media'] = media

if studentData['media'] >= 60:
    studentData['situacao'] = 'AP'
else:
    studentData['situacao'] = 'RP'

print('Situação final do aluno: ', studentData['situacao'])
print(studentData)    