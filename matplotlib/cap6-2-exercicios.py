import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def delimiter():
    print('---------------------------------')


# Questão 2)
print(f'Questão 2')

paises = pd.read_csv('arquivos/paises.csv', delimiter=';')

# Removendo espaços em branco extras na coluna 'Region'
paises['Region'] = paises['Region'].str.strip()

# Filtrar países da América do Norte
paisesNA = paises[paises['Region'] == 'NORTHERN AMERICA']


# Gráfico de linha para a taxa de mortalidade
plt.plot(paisesNA['Country'], paisesNA['Deathrate'],
         label='Taxa de Mortalidade', marker='o')

# Gráfico de linha para a taxa de natalidade
plt.plot(paisesNA['Country'], paisesNA['Birthrate'],
         label='Taxa de Natalidade', marker='o')

# Configurar o gráfico
plt.xlabel('País')
plt.ylabel('Taxa')
plt.title('Taxa de Mortalidade e Natalidade na América do Norte')
plt.legend()  # Adicionar legenda

# Exibir o gráfico
plt.tight_layout()
plt.show()
