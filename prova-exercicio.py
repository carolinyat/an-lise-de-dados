import numpy as np

arr = np.loadtxt('arquivos/paises.csv', delimiter=';',
                 dtype=str, encoding='utf-8')


def converterFloat(valor):
    try:
        return float(valor)
    except ValueError:
        return 0.0


def limiter():
    print('---------------------------------')


# Exercício 1

print(f'Exercício 1')

# Índices das colunas com os rótulos desejados
indices = [0, 1, 2, 3]

# Slicing para obter as colunas desejadas
dados = arr[:, indices]

# Remover espaços extras ao redor das entradas dos dados
dados = np.char.strip(dados)

# Exibindo os dados
print(dados)

limiter()

# Exercício 2

print(f'Exercício 2')

regioes = arr[:, 1]  # coluna 2

# Remover entradas de regiões que contenham "Region"
regioes = regioes[regioes != 'Region']
# Remover espaços extras ao redor das entradas das regiões
regioes = np.char.strip(regioes)

uniqueRegioes = np.unique(regioes)

totalRegioes = len(uniqueRegioes)

print(f'As regiões são: {uniqueRegioes}, totalizando {totalRegioes} regiões.')

limiter()

# Exercício 3

print(f'Exercício 3')

literacy = arr[:, 9]

literacy = np.array([converterFloat(valor) for valor in literacy])

media = np.mean(literacy)

print(f'Média da taxa de alfabetização: {media:.2f}')

limiter()

# Exercício 4

print(f'Exercício 4')

paises = arr[:, 0]
regiao = arr[:, 1]

# verifica se cada elemento da matriz regiao é igual a NORTHERN AMERICA após remover os espaços em branco (strip)
# americaNorte = np.sum([reg.strip() == 'NORTHERN AMERICA' for reg in regiao])

regiao = np.char.strip(regiao)
americaNorte = np.sum(regiao == 'NORTHERN AMERICA')

print(f'Número de países na América do Norte: {americaNorte}')

limiter()

# Exercício 5

print(f'Exercício 5')

paises = arr[:, 0]
regioes = arr[:, 1]
rendas = arr[:, 8]

latinAmerCarib = np.where(regioes == 'LATIN AMER. & CARIB')

if len(latinAmerCarib) > 0:
    valores = np.array([converterFloat(renda) for renda in rendas])
    indiceMaisCara = np.argmax(valores[latinAmerCarib])
    rendaMaisAlta = valores[latinAmerCarib][indiceMaisCara]

print(f'A maior renda per capita per capita é: {rendaMaisAlta}')


