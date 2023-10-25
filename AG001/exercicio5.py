import sympy as sp

# Valor de c = 136 % 10 = 6
c = 6 

x = sp.symbols('x')

# Equação 1: 2x + 24x = c + 1
equacao1 = 2*x + 24*x - (c + 1)

# Solução para a Equação 1
solucao1 = sp.solve(equacao1, x)
print("Solução para a Equação 1:")
for sol in solucao1:
    print(f"x = {sol}")

# Equação 2: 5*sqrt(x) - 4*x**2 + x**2 = c
equacao2 = 5*sp.sqrt(x) - 4*x**2 + x**2 - c

# Solução para a Equação 2
solucao2 = sp.solve(equacao2, x)
print("\nSolução para a Equação 2:")
for sol in solucao2:
    print(f"x = {sol}")

# Equação 3: (3*tan((c-3)*x) + 2)**2 = 0
equacao3 = (3*sp.tan((c-3)*x) + 2)**2

# Solução para a Equação 3
solucao3 = sp.solve(equacao3, x)
print("\nSolução para a Equação 3:")
for sol in solucao3:
    print(f"x = {sol}")
