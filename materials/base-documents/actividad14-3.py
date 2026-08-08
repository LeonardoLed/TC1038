import matplotlib.pyplot as plt
import numpy as np

# agrega tus comentarios

x = np.random.randint(1, 100, 10)
y = np.random.randint(1, 100, 10)


plt.scatter(x, y, color='blue', marker='o', label='Puntos')

plt.title('Gráfica de Dispersión (Scatterplot)')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()

plt.show()
