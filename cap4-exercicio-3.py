import numpy as np

arr = np.loadtxt('arquivos/space.csv',
                 delimiter=';', dtype=str, encoding='utf-8')

def delimiter():
    print("------------------------------------------------------------------------------------------------------------------")

def converterFloat(valor):
    try:
        return float(valor)
    except ValueError:
        return 0.0  # Retorna 0 para valores não numéricos

# Exercício 1
# valores_unicos = np.unique(arr[:, 7])
# print("Valores únicos na coluna 'status mission':", valores_unicos)

print(f"Exercício 1")

# 8ª coluna (índice 7)
statusMissao = arr[:, 7]

# quantas missões tiveram sucesso
sucesso = np.sum(statusMissao == 'Success')

# porcentagem de missões bem-sucedidas
totalMissoes = len(statusMissao)
porcentagemSucesso = (sucesso * 100) / totalMissoes

print(
    f"A porcentagem de missões bem-sucedidas é de {porcentagemSucesso:.2f}%")

delimiter()

# Exercício 2

print(f"Exercício 2")

# 7ª coluna (índice 6)
valoresGastos = arr[:, 6]

valoresGastos = np.array([converterFloat(valor) for valor in valoresGastos])

valoresGastos_positivos = valoresGastos[valoresGastos > 0]

mediaGastos = np.mean(valoresGastos_positivos)

print(
    f"A média de gastos das missões com valores positivos é de U$ {mediaGastos:.2f}")

delimiter()

# Exercício 3

print(f"Exercício 3")

localidades = arr[:, 2]

missoesEUA = np.sum(np.char.find(localidades, 'USA') >= 0)

print(
    f"Foram realizadas {missoesEUA} missões espaciais nos Estados Unidos.")

delimiter()

# Exercício 4

print(f"Exercício 4")

empresas = arr[:, 1]  # 2ª coluna (índice 1)
custos = arr[:, 6]    # 7ª coluna (índice 6) 

# filtrar apenas as missões da SpaceX
indicesSpaceX = np.where(empresas == 'SpaceX')

if len(indicesSpaceX) > 0:
    custos_float = np.array([converterFloat(custo) for custo in custos])

    # índice da missão mais cara da SpaceX
    indiceMaisCara = np.argmax(custos_float[indicesSpaceX])


    # custo da missão mais cara da SpaceX
    custoMaisCara = custos_float[indicesSpaceX][indiceMaisCara]

print(f"A missão mais cara da SpaceX foi com um custo de {custoMaisCara:.2f} dólares.")

delimiter()

# Exercício 5

print(f"Exercício 5")

empresas = arr[:, 1]  # 2ª coluna (índice 1) 

# obter valores únicos (nomes de empresas)
uniqueEmpresas = np.unique(empresas)

# dicionário para rastrear a contagem de missões por empresa
missaoEmpresa = {}

# preenchendo o dicionário com a contagem de missões por empresa
for empresa in uniqueEmpresas:
    # Contagem de missões para esta empresa
    contagem = np.sum(empresas == empresa)
    missaoEmpresa[empresa] = contagem

# loop for para mostrar as informações
for empresa, contagem in missaoEmpresa.items():
    print(f"Empresa: {empresa} | Missões realizadas: {contagem}")

delimiter()
