import sympy as sp
from scipy import integrate

# Defina as variáveis e o valor de c
x = sp.symbols('x')
c = 136 % 10  # c é igual ao resto da divisão de 136 por 10, ou seja, c = 6

# Função
f_x = x**3 - 4*x**2 + 5*x - c

# Converte a função simbólica em uma função numérica
f_numeric = sp.lambdify(x, f_x, "numpy")

a = 0  # Limite inferior
b = 5  # Limite superior

# Calculo da área
area = integrate.quad(f_numeric, a, b)[0]

print("Área sob a curva:", area)
