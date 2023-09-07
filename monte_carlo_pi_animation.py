from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.animation as animation
from matplotlib import rcParams

# Set matplotlib configuration for better visualization
rcParams['mathtext.fontset'] = 'cm'
rcParams['font.size'] = 14

# Define colors
red = "#e41a1c"
blue = "#377eb8"
gray = "#eeeeee"

# Function to update the animation frame
def update(n):
    ax.cla()  # Clear the previous frame
    pts = np.random.uniform(low=0, high=1, size=(2, n))
    circ = pts[:, pts[0, :]**2 + pts[1, :]**2 <= 1]
    out_circ = pts[:, pts[0, :]**2 + pts[1, :]**2 > 1]
    pi_approx = 4 * circ.shape[1] / n
    
    # Create a quarter-circle patch
    circle = mpatches.Wedge((0, 0), 1, 0, 90, color=gray)
    ax.add_artist(circle)
    
    # Plot points inside and outside the quarter-circle
    plt.plot(circ[0, :], circ[1, :], marker='.', markersize=1, linewidth=0, color=red)
    plt.plot(out_circ[0, :], out_circ[1, :], marker='.', markersize=1, linewidth=0, color=blue)
    
    # Set title and axis properties
    plt.title(r"$n = {}, \pi \approx {:.4f}$".format(n, pi_approx))
    plt.axis("square")
    plt.xlim(0, 1)
    plt.ylim(0, 1)

# Define the values of n for animation frames
nvec = [3000, 4000, 5000, 6500, 8500, 10000, 15000, 18000, 24000, 30000]

# Create a figure and subplot
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111)

# Create the animation using Pillow (PIL) writer
ani = animation.FuncAnimation(fig, update, frames=nvec, blit=False)

# Save the animation as a GIF using the Pillow (PIL) writer
ani.save("monte_carlo_pi.gif", writer='pillow', fps=15)  # Adjust the fps as needed
