import matplotlib.pyplot as plt
import numpy as np

# Define x values
x_values = np.linspace(-10, 10, 100)

# Define the linear function y = 2x + 3
y_values = 2 * x_values + 3

# Plot the line
plt.plot(x_values, y_values, label='y = 2x + 3')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Function: y = 2x + 3')

# Add grid
plt.grid(True)

# Add legend
plt.legend()

# Show plot
plt.show()
