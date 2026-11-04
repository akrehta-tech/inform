import numpy as np
import matplotlib.pyplot as plt


dist = np.array([100, 500, 1000, 3000, 5000, 10000])   # км
ping = np.array([1.8, 5.9, 11.5, 32.5, 53.0, 104.2])   # мс


c = 300000.0
n = 1.5
v = c / n

d_line = np.linspace(0, dist.max(), 200)
ping_theory = (2 * d_line / v) * 1000


fig, ax = plt.subplots(figsize=(10, 6))


ax.plot(dist, ping, linestyle='None', marker='o', markersize=9,
        markerfacecolor='crimson', markeredgecolor='darkred',
        label='Измеренный пинг')


ax.plot(d_line, ping_theory, linestyle='-', color='navy', linewidth=2,
        label=f'Теория: v = c/n = {v:.0f} км/с')


ax.set_title("Оптоволокно: измеренный и теоретический пинг",
             fontsize=15, fontweight='bold')
ax.set_xlabel("Расстояние, км", fontsize=12)
ax.set_ylabel("Пинг (RTT), мс", fontsize=12)

ax.set_xlim(0, dist.max() * 1.05)
ax.set_ylim(0, ping.max() * 1.05)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig('ping_test.png', dpi=150)

plt.show()
