import numpy as np
import random

def delimiter():
    print("------------------------------------------------------------------------------------------------------------------")

# Exercicio 1

# semente para garantir que os resultados sejam reprodutíveis
random.seed(5)

# array de 10 floats entre -1 e 1
arrayOriginal = np.random.uniform(-1, 1, 10)

arrayMultiplicado = arrayOriginal * 100

# vetor com a parte inteira dos números
arrayInteiro = np.floor(arrayMultiplicado).astype(int)

print("\nArray original:")
print(arrayOriginal)

print("\nArray multiplicado por 100:")
print(arrayMultiplicado)

print("\nArray apenas com a parte inteira:")
print(arrayInteiro)

delimiter()

# Exercicio 2

random.seed(10)

matriz = np.random.randint(1, 51, (4, 4))

print("\nMatriz:")
print(matriz)

delimiter()


# Exercicio 3

mediaLinhas = np.mean(matriz, axis=1)

# Calcule a média de cada coluna
mediaColunas = np.mean(matriz, axis=0)

print("\nMédias das linhas:")
print(mediaLinhas)

print("\nMédias das colunas:")
print(mediaColunas)

# Encontre o maior valor entre as médias das linhas e colunas
maiorMediaLinhas = np.max(mediaLinhas)
maiorMediaColunas = np.max(mediaColunas)

print("\nMaior média das Linhas:", maiorMediaLinhas)
print("Maior média das Colunas:", maiorMediaColunas)

delimiter()

# Exercicio 4

contNum = np.bincount(matriz.ravel())

# Mostre apenas os números que aparecem duas vezes
contNumTwice = np.where(contNum == 2)[0]

print("\nContagem de aparições de cada número:")
for numero, quantidade in enumerate(contNum):
    if quantidade > 0:
        print(f"O número {numero} aparece {quantidade} vezes.")

print("\nNúmeros que aparecem duas vezes:")
print(contNumTwice)
