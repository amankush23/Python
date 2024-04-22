import matplotlib.pyplot as plt
import numpy as np

# Define x values
x_values = np.linspace(0, 2*np.pi, 100)

# Define the functions
y_sin = np.sin(x_values)
y_cos = np.cos(x_values)
y_tan = np.tan(x_values)

# Plot the functions
plt.plot(x_values, y_sin, label='$y = \sin(x)$', color='blue')
plt.plot(x_values, y_cos, label='$y = \cos(x)$', color='red')
plt.plot(x_values, y_tan, label='$y = \tan(x)$', color='green')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trigonometric Functions: $\sin(x)$, $\cos(x)$, and $\tan(x)$')

# Set y-axis limits for better visualization of tan(x)
plt.ylim(-2, 2)

# Add grid
plt.grid(True)

# Add legend
plt.legend()

# Show plot
plt.show()
