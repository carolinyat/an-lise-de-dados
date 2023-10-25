import numpy as np
def delimiter():
    print("------------------------------------------------------------------------------------------------------------------")

# Exercicio 1
print('Array de tamanho 21 com valores linearmente espaçados entre 0 e 1: ')
arr = np.linspace(0, 1, 21)
print(arr)

delimiter()

# Exercicio 2

arr1 = np.arange(0, 51, 2)
arr2 = np.arange(100, 50, -2)

concatenated = np.concatenate((arr1,arr2))
concatenated = np.sort(concatenated)

print('Array ordenado de forma cresente: ')
print(concatenated)

delimiter()

# Exercicio 3
concatenated = np.flip(np.sort(concatenated))
print('Array ordenado de forma descresente: ')
print(concatenated)

delimiter()

# Exercicio 4
matriz = np.ones((3, 4), dtype=int)

array_1d = matriz.flatten()

print("Matriz 3x4 de '1's:")
print(matriz)

print("\nArray 1D:")
print(array_1d)

delimiter()

# Exercicio 5
matriz = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15]])

# número de linhas e colunas da matriz
num_linhas, num_colunas = matriz.shape

# multiplique o número de linhas e colunas
produto = num_linhas * num_colunas

# se o produto é par ou ímpar
if produto % 2 == 0:
    print(f"A matriz pode ser convertida em um vetor com um número par de elementos ({produto} elementos).")
else:
    print(f"A matriz pode ser convertida em um vetor com um número ímpar de elementos ({produto} elementos).")