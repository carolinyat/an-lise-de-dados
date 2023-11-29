import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def delimiter():
    print('---------------------------------')

# Questão 1
print(f'Questão 1')

# Carregar o dataset
paises = pd.read_csv('arquivos/space.csv', delimiter=';')

# Filtrar empresas dos EUA e China
empresasEUA = paises[paises['Location'].str.contains('USA')]['Company Name'].unique()
empresasChina = paises[paises['Location'].str.contains('China')]['Company Name'].unique()

# print(empresasEUA, empresasChina)

# Contabilizando o número de empresas em cada país
qtdEmpresasEUA = len(empresasEUA)
qtdEmpresasChina = len(empresasChina)

# Criando o gráfico
countries = ['EUA', 'China']
counts = [qtdEmpresasEUA, qtdEmpresasChina]

plt.bar(countries, counts, color=['blue', 'red'])
plt.xlabel('País')
plt.ylabel('Número de Empresas Espaciais')
plt.title('Número de Empresas Espaciais nos EUA e na China')
# plt.show()

delimiter()

# Questão 2)
print(f'Questão 2')

paises = pd.read_csv('arquivos/paises.csv', delimiter=';')

# Removendo espaços em branco extras na coluna 'Region'
paises['Region'] = paises['Region'].str.strip()

# Filtrar países da América do Norte
paisesNA = paises[paises['Region'] == 'NORTHERN AMERICA']


# Gráfico de linha para a taxa de mortalidade
plt.plot(paisesNA['Country'], paisesNA['Deathrate'], label='Taxa de Mortalidade', marker='o')

# Gráfico de linha para a taxa de natalidade
plt.plot(paisesNA['Country'], paisesNA['Birthrate'], label='Taxa de Natalidade', marker='o')

# Configurar o gráfico
plt.xlabel('País')
plt.ylabel('Taxa')
plt.title('Taxa de Mortalidade e Natalidade na América do Norte')
plt.legend()  # Adicionar legenda

# Exibir o gráfico
plt.tight_layout()
plt.show()