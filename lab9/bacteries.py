import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t_stop = 20 * np.log2(1000)
t = np.linspace(0, t_stop, 400)
N = 2 ** (t / 20)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.set_title("Обычная шкала: «незаметно -> БУМ!»", fontsize=11)
ax1.set_xlabel("Минуты")
ax1.set_ylabel("Бактерий")
ax1.set_xlim(0, 205)
ax1.set_ylim(0, 1080)
ax1.grid(True, alpha=0.3)

ax2.set_title("Лог-шкала: ровная прямая", fontsize=11)
ax2.set_xlabel("Минуты")
ax2.set_ylabel("Бактерий (log)")
ax2.set_yscale('log')
ax2.set_xlim(0, 205)
ax2.set_ylim(1, 1300)
ax2.grid(True, which="both", alpha=0.3)

for ax in (ax1, ax2):
    ax.axhline(1000, ls='--', color='red', lw=1.2)
    ax.plot(t, N, color='green', lw=1.5, zorder=1, alpha=0.3)

line1, = ax1.plot([], [], color='green', lw=2, zorder=2)
dot1, = ax1.plot([], [], marker='o', markersize=7, color='green', zorder=3)
text1 = ax1.text(0.03, 0.94, "", transform=ax1.transAxes, va='top', family='monospace', fontsize=9)

line2, = ax2.plot([], [], color='green', lw=2, zorder=2)
dot2, = ax2.plot([], [], marker='o', markersize=7, color='green', zorder=3)
text2 = ax2.text(0.03, 0.94, "", transform=ax2.transAxes, va='top', family='monospace', fontsize=9)

last_frame = len(t) - 1

def update(frame):
    n = frame + 1
    curr_t = t[frame]
    curr_N = N[frame]
    
    line1.set_data(t[:n], N[:n])
    dot1.set_data([curr_t], [curr_N])
    
    line2.set_data(t[:n], N[:n])
    dot2.set_data([curr_t], [curr_N])
    
    info = f"t = {curr_t:.1f} мин\nN = {int(round(curr_N))}"
    text1.set_text(info)
    text2.set_text(info)
    
    if frame == last_frame:
        for dot in (dot1, dot2):
            dot.set_color('red')
            dot.set_markersize(11)
        hours = int(curr_t // 60)
        mins = curr_t % 60
        fig.suptitle(f"Порог 1000 достигнут за {curr_t:.1f} мин ({hours} ч {mins:.1f} мин)!", 
                     fontsize=13, fontweight='bold', color='darkred')
        
    return line1, dot1, text1, line2, dot2, text2

ani = FuncAnimation(fig, update, frames=len(t), interval=20, blit=False, repeat=False)

plt.tight_layout()
plt.show()
