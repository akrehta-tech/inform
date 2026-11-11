import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots(figsize=(8, 8))
t = np.linspace(0, 2*np.pi, 250)
x = [16*np.sin(point)**3 for point in t]
y = [13*np.cos(point) - 5*np.cos(2*point) - 2*np.cos(3*point) - np.cos(4*point) for point in t]
ax.set_xlim(np.min(x) - 2, np.max(x) + 2)
ax.set_ylim(np.min(y) - 2, np.max(y) + 2)
ax.axis('off')

line, = ax.plot([], [], color='red', lw=2.5)

def update(frame):
    line.set_data(x[:frame], y[:frame])
    return line,

ani = FuncAnimation(fig, update, frames=len(t) + 1, interval=30, repeat=False)
plt.show()
