import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0,5,100)
y = x**3
plt.plot(x,y, "r--", label = "$x^3$", linewidth = 5)
plt.title("Función en python con numpy y matplotlib")
plt.legend()
plt.grid()
plt.show()


