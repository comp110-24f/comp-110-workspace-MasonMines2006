# Import libraries
import numpy as np

# For displaying data
import matplotlib.pyplot as plt  # 2d simulation


# Generate a 25x25 Meshgrid with 2500 total values between 0 and 10
xvalues = np.linspace(0, 10, num=25)
yvalues = np.linspace(0, 10, num=25)

# Create the grid
x_mesh, y_mesh = np.meshgrid(xvalues, yvalues)

# Plot the grid points with pyplot
plt.plot(x_mesh, y_mesh, marker="o", color="k", linestyle="none")
plt.show()
