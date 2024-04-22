import matplotlib.pyplot as plt
import numpy as np

t_values = np.linspace(0, 2 * np.pi , 100)
Cos = np.cos(t_values)
sin = np.sin(t_values)
plt.title('Plotting Parametric Equations')
plt.xlabel('x data')
plt.ylabel('y data')
plt.plot(t_values,Cos, label = 'equation\'s line',color = 'r',ls = 'dotted')
plt.plot(t_values,sin, label = 'equation\'s line',color = 'r',ls = 'dotted')
plt.grid(True)
plt.legend()
# plt.axvline(0)
# plt.axhline(0)
plt.show()import matplotlib.pyplot as plt
import numpy as np

t_values = np.linspace(0, 2 * np.pi , 100)
Cos = np.cos(t_values)
sin = np.sin(t_values)
plt.title('Plotting Parametric Equations')
plt.xlabel('x data')
plt.ylabel('y data')
plt.plot(t_values,Cos, label = 'equation\'s line',color = 'r',ls = 'dotted')
plt.plot(t_values,sin, label = 'equation\'s line',color = 'r',ls = 'dotted')
plt.grid(True)
plt.legend()
# plt.axvline(0)
# plt.axhline(0)
plt.show()