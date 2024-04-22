import matplotlib.pyplot as plt
import numpy as np

# Define x values
x_values = np.linspace(-5, 5, 100)

# Define the function
y_values = np.exp(x_values)

# Plot the function
plt.plot(x_values, y_values, label='$y = e^x$', color='blue')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Exponential Function: $y = e^x$')

# Add grid
plt.grid(True)

# Add legend
plt.legend()

# Show plot
plt.show()
