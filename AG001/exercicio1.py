import sympy as sp

# Defina as variáveis e o valor de c
x = sp.symbols('x')
c = 136 % 10  # c é igual ao resto da divisão de 136 por 10, ou seja, c = 6

expression1 = (1 + (c + 4) / x**3)**(x**3)

limit_value1 = sp.limit(expression1, x, 0)

print('Resultado 1: ', limit_value1)

expression2 = (1 + (c + 4) / x**3)**(x**3)

limit_value2 = sp.limit(expression2, x, sp.oo)

print('Resultado 2: ', limit_value2)

expression3 = expression = (1 + (c + 4) / x**3)**(x**3)

limit_value3 = sp.limit(expression3, x, -sp.oo)

print('Resultado 3: ', limit_value3)