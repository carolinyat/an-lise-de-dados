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