import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(-5,5,100)
y_values = np.exp(x_values)
plt.title('Linear function')
plt.xlabel('x data')
plt.ylabel('y data')
plt.plot(x_values, y_values, label = 'Exponential',color = 'r',ls = 'dotted')
plt.grid(True)
plt.legend()
plt.axvline(0)
plt.axhline(0)
plt.show()