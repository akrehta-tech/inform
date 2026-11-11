import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots(figsize=(8, 6))

x = np.linspace(0, 20, 400)
R = -2*x**2 + 40*x
peak_idx = int(np.argmax(R))
shadow, = ax.plot(x, R, 'b-', alpha=0.2)
pt, = ax.plot([], [], 'ro', markersize=10)
line, = ax.plot([], [], 'r-', lw=2)
info_text = ax.text(0.05, 0.92, '', transform=ax.transAxes, fontsize=12)

ax.set_xlim(0, 22)
ax.set_ylim(0, max(R) + 20)
ax.set_title("Выручка от лимонада")
ax.set_xlabel("Цена за стакан, x")
ax.set_ylabel("Выручка R(x)")
ax.grid(True, alpha=0.3)

def update(frame):
    line.set_data(x[:frame+1], R[:frame+1])
    pt.set_data([x[frame]], R[[frame]])
    info_text.set_text(f"цена = {x[frame]:.1f}  выручка = {R[frame]:.1f}")
    if frame == peak_idx:
        line.set_color('yellow')
        pt.set_color('yellow')
    return line, pt

ani = FuncAnimation(fig, update, repeat=False, frames=peak_idx + 1, interval=20)

plt.show()
