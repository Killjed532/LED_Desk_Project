import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and an axes
fig, ax = plt.subplots()

# Initial color matrix with zeros
color_matrix = np.zeros((50, 30, 3))  # 10x10 matrix with 3 channels (RGB)

# Function to update the figure
def update(frame):
    color_matrix = np.random.rand(50, 30, 3)  # Generate a new color matrix
    ax.clear()  # Clear the previous image
    ax.imshow(color_matrix)  # Display the color matrix
    ax.axis('off')  # Hide the axes

# Create an animation
ani = FuncAnimation(fig, update, frames=range(100), interval=100)

# Save the animation as a GIF
ani.save('new_color_matrix_animation.gif', writer='pillow', fps=10)

plt.close()

