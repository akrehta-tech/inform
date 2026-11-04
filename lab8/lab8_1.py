import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 15)
day_temp = [5.1, 6.3, 4.8, 7.2, 9.5, 8.1, 6.7, 5.9, 7.4, 8.8, 10.2, 9.1, 7.5, 6.2]
night_temp = [-1.2, 0.3, -2.1, 1.5, 3.8, 2.4, 0.9, -0.4, 1.8, 3.2, 4.6, 2.9, 1.1, -0.3]


day_mean = np.mean(day_temp)
night_mean = np.mean(night_temp)
frost_nights = sum(1 for t in night_temp if t < 0)

plt.figure(figsize=(12, 6))

plt.plot(days, day_temp, color='tab:orange', linestyle='-', marker='o',
         label='Днём (14:00)', linewidth=2, markersize=6)
plt.plot(days, night_temp, color='tab:blue', linestyle='--', marker='s',
         label='Ночью (02:00)', linewidth=2, markersize=6)


plt.axhline(day_mean, color='tab:orange', linestyle=':', linewidth=1.5,
            label=f'Среднее днём = {day_mean:.2f} °C')
plt.axhline(night_mean, color='tab:blue', linestyle=':', linewidth=1.5,
            label=f'Среднее ночью = {night_mean:.2f} °C')


plt.axhline(0, color='black', linestyle='-', linewidth=1, alpha=0.6,
            label='y = 0 (граница мороза)')


plt.title('Температура воздуха днём и ночью (14 дней)', fontsize=14)
plt.xlabel('День', fontsize=12)
plt.ylabel('Температура, °C', fontsize=12)
plt.xticks(days)
plt.grid(True, alpha=0.4)
plt.legend(loc='upper left', fontsize=9)
plt.tight_layout()


plt.savefig('weather.png', dpi=150)
plt.show()

print(f'Средняя дневная температура: {day_mean:.2f} °C')
print(f'Средняя ночная температура:  {night_mean:.2f} °C')
print(f'Ночей с температурой ниже нуля:', frost_nights)
