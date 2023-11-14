import pandas as pd

def delimiter():
    print('---------------------------------')

paises = pd.read_csv('arquivos/paises.csv', delimiter=';')

# Questão 1 a)
print(f'Questão 1 - letra a)')

# Removendo espaços em branco extras na coluna 'Region'
paises['Region'] = paises['Region'].str.strip()

# Filtrando os países da Oceania
paisesOceania = paises[paises['Region'] == 'OCEANIA']['Country']

print(paisesOceania)

delimiter()

# Questão 1 b)
print(f'Questão 1 - letra b)')

# Contando o número de países da Oceania
num_paisesOceania = paises['Region'].str.contains('OCEANIA').sum()

print(f"Total de países da Oceania: {num_paisesOceania}")

delimiter()

# Questão 2
print(f'Questão 2')

# Calculando a média da taxa de alfabetização
mediaAlfabetizacao = paises['Literacy (%)'].mean()

print(f'Média da taxa de alfabetização: {mediaAlfabetizacao:.2f}%')

delimiter()

# Questão 3
print(f'Questão 3')

# Encontrando o índice do país com a maior população
indiceMax = paises['Population'].idxmax()

# Obtendo o nome e a região do país com a maior população
paisMaiorPop = paises.loc[indiceMax, ['Country', 'Region']]

print(f'País com a maior população:\n{paisMaiorPop}')

delimiter()

# Questão 4
print(f'Questão 4')

# Filtrando os países sem costa marítima
paisesSemCosta = paises[paises['Coastline (coast/area ratio)'] == 0]

# Salvando os países sem costa em um novo arquivo CSV
caminhoArq = 'arquivos/noCoast.csv'
paisesSemCosta.to_csv(caminhoArq, index=False)

print(paisesSemCosta[['Country', 'Coastline (coast/area ratio)']])

# print(f'\nOs países sem costa foram salvos em: {caminhoArq}')