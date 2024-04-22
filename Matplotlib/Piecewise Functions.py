import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(-5,5,100)
y_values = np.where(x_values < 0, 0, 1)
plt.title('Plotting Piecewise Functions')
plt.xlabel('x data')
plt.ylabel('y data')
plt.plot(x_values, y_values, label = 'linear line',color = 'r',ls = 'dotted')
plt.grid(True)
plt.legend()
# plt.axvline(0)
# plt.axhline(0)
plt.show()