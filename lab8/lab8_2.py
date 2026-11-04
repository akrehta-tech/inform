import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 15)
screen_hours = [4.5, 5.2, 5.8, 4.9, 6.1, 6.8, 7.2, 7.5, 8.1, 7.8, 8.5, 9.0, 9.3, 9.7]
battery = [58, 52, 48, 55, 42, 38, 33, 29, 22, 25, 18, 14, 11, 8]


screen_mean = np.mean(screen_hours)
battery_mean = np.mean(battery)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))


ax1.plot(days, screen_hours, color='tab:green', linestyle='-', marker='o',
         linewidth=2, markersize=6, label='Экранное время')
ax1.axhline(screen_mean, color='tab:red', linestyle='--', linewidth=1.5,
            label=f'Среднее = {screen_mean:.2f} ч')
ax1.set_title('Экранное время по дням', fontsize=13)
ax1.set_xlabel('День', fontsize=11)
ax1.set_ylabel('Часы, ч', fontsize=11)
ax1.set_xticks(days)
ax1.set_ylim(0, 11)
ax1.grid(True, alpha=0.4)
ax1.legend(loc='upper left', fontsize=9)


ax2.plot(days, battery, color='tab:purple', linestyle='-', marker='s',
         linewidth=2, markersize=6, label='Заряд батареи')
ax2.axhline(battery_mean, color='tab:red', linestyle='--', linewidth=1.5,
            label=f'Среднее = {battery_mean:.2f} %')
ax2.set_title('Заряд батареи к концу дня', fontsize=13)
ax2.set_xlabel('День', fontsize=11)
ax2.set_ylabel('Заряд, %', fontsize=11)
ax2.set_xticks(days)
ax2.set_ylim(0, 100)
ax2.grid(True, alpha=0.4)
ax2.legend(loc='upper right', fontsize=9)

plt.tight_layout()
plt.savefig('phone.png', dpi=150)
plt.show()
