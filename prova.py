import numpy as np

arr = np.loadtxt('arquivos/shopping_trends.csv',
                 delimiter=',', dtype=str, encoding='utf-8')


def delimiter():
    print('------------------------------------------------------------------------')


def converterFloat(valor):
    try:
        return float(valor)
    except ValueError:
        return 0.0

# Exercício 1


print(f'Exercício 1')

idades = arr[:, 1]

idades = np.array([converterFloat(valor) for valor in idades])

media = np.mean(idades)

print(f'A média de idades é: {media:.2f}')

delimiter()

# Exercício 2

print(f'Exercício 2')

valorGasto = arr[:, 5]

valorGasto = np.array([converterFloat(valor) for valor in valorGasto])
media = np.mean(valorGasto)
# print(media)

resultado = np.sum(valorGasto > media)

print(f'Clientes que gastaram mais que a média de gastos de compra: {resultado}')

delimiter()

# Exercício 3

print(f'Exercício 3')

items = arr[:, 3]

total = len(items)
# print(total)
menosVendido = np.argmin(items)
# print(menosVendido)

porcentagem = (menosVendido * 100) / total
print(f'A porcentagem do item menos vendido é: {porcentagem:.2f}%')

delimiter()

# Exercício 4

print(f'Exercício 4')

descontos = arr[:, 13]

total = len(descontos)
# print(total)
descontoPositivo = np.sum(descontos == 'Yes')
# print(descontoPositivo)

porcentagem = (descontoPositivo * 100) / total
print(f'A porcentagem das compras que tiveram desconto é de: {porcentagem:.2f}%')

delimiter()

# Exercício 5 

print(f'Exercício 5')

cores = arr[:, 8]
estacao = arr[:, 9]

verao = np.where(estacao == 'Summer')

indiceMaisUsado = np.argmax(cores[verao])
corMaisUsada = cores[verao][indiceMaisUsado]

print(f'A cor mais usada no verão é: {corMaisUsada}')



