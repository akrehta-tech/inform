import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_title("Случайное блуждание")
ax.grid(True, linestyle="--", alpha=0.5)

x_data, y_data = [0.0], [0.0]

line, = ax.plot([], [], "b-", lw=1.5)
robot, = ax.plot([], [], "ro", markersize=8)

def update(frame):
    dx = random.uniform(-2, 2)
    dy = random.uniform(-2, 2)

    new_x = x_data[-1] + dx
    new_y = y_data[-1] + dy
    x_data.append(new_x)
    y_data.append(new_y)

    line.set_data(x_data, y_data)
    robot.set_data([new_x], [new_y])

    indent = 2
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    if new_x < xlim[0] + indent or new_x > xlim[1] - indent or new_y < ylim[0] + indent or new_y > ylim[1] - indent:
        ax.set_xlim(min(x_data) - indent, max(x_data) + indent)
        ax.set_ylim(min(y_data) - indent, max(y_data) + indent)
        fig.canvas.draw()

    return line, robot


ani = animation.FuncAnimation(fig, update, frames=300, interval=40, blit=False)

plt.show()
