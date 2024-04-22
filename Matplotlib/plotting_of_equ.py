import matplotlib.pyplot as plt
import numpy as np

# Define x values
x_values = np.linspace(0, 10, 100)

# Define the functions
y1_values = x_values ** 2  # y = x^2
y2_values = np.sqrt(x_values)  # y = sqrt(x)

# Plot the functions
plt.plot(x_values, y1_values, label='$y = x^2$', color='blue', linestyle='-')
plt.plot(x_values, y2_values, label='$y = \sqrt{x}$', color='red', linestyle='--')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $y = x^2$ and $y = \sqrt{x}$')

# Add grid
plt.grid(True)

# Add legend
plt.legend()

# Show plot
plt.show()
