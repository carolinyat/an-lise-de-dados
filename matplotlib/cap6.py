import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Criando um plot
x = np.array([1, 2, 3, 4])
y = x*2 # broadcasting

plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

plt.plot(x, y, '*--m', markersize=10, linewidth=2) #plot
plt.show() # mostrando o plot