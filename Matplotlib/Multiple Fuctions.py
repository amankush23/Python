import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(0,10,100)
y_values = x_values ** 2
y_values2 = np.sqrt(x_values)
plt.title('Multiple Fuctions')
plt.xlabel('x data')
plt.ylabel('y data')
plt.plot(x_values, y_values, label = 'Power',color = 'r',ls = 'dotted')
plt.plot(x_values, y_values2, label = 'square root',color = 'g')
plt.grid(True)
plt.legend()
# plt.axvline(0)
# plt.axhline(0)
plt.show()