import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(-10,10,100)
y_values = 2 * x_values + 3
plt.title('Linear function')
plt.xlabel('x data')
plt.ylabel('y data')
plt.plot(x_values, y_values, label = 'linear line',color = 'r',ls = 'dotted')
plt.grid(True)
plt.legend()
plt.axvline(0)
plt.axhline(0)
plt.show()