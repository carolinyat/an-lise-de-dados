import sympy as sp

A = 15 / 100  # Amplitude em metros 
frequencia = 20  # Frequência em Hz
c = 136 % 10  # c é igual ao resto da divisão de 136 por 10, ou seja, c = 6

# Frequência angular
omega = 2 * sp.pi * frequencia

# Tempo
t = sp.symbols('t')

# Equação do deslocamento
deslocamento = A * sp.cos(omega * t)

# Equação da velocidade
velocidade = -A * omega * sp.sin(omega * t)

# Equação da aceleração
aceleracao = -A * omega**2 * sp.cos(omega * t)

# Aceleração em t = 10 segundos
tempo_10s = 10
aceleracao_em_10s = aceleracao.subs(t, tempo_10s)

print("Equação do Deslocamento (x(t)): ", deslocamento)
print("Equação da Velocidade (v(t)): ", velocidade)
print("Equação da Aceleração (a(t)): ", aceleracao)
print(f"Aceleração em t = {tempo_10s} segundos: {aceleracao_em_10s:.2f} m/s²")
