import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Расчёт точки остановки (когда T = 40°C)
t_stop = -20 * np.log(20 / 70)  # ≈ 25.06 мин

# Данные для полной фоновой кривой (с небольшим запасом, как на превью) и для анимации
t_full = np.linspace(0, 26.5, 400)
T_full = 20 + 70 * np.exp(-0.05 * t_full)

t_anim = np.linspace(0, t_stop, 300)
T_anim = 20 + 70 * np.exp(-0.05 * t_anim)

# 2. Настройка графика
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.set_xlim(0, 27.5)
ax.set_ylim(15, 95)

ax.set_title("Чай остывает по закону Ньютона", fontsize=12)
ax.set_xlabel("Минуты")
ax.set_ylabel("Температура, °C")
ax.grid(True, alpha=0.3)

# Бледная фоновая кривая
ax.plot(t_full, T_full, color='#d8cfc8', lw=2, zorder=1)

# Горизонтальные линии уровней (питьевая и комнатная температура)
ax.axhline(40, ls='--', color='orange', lw=1.2, alpha=0.8)
ax.text(0.5, 41.5, "питьевая 40°C", color='orange', fontsize=9)

ax.axhline(20, ls='--', color='royalblue', lw=1.2)
ax.text(13.8, 21.5, "комнатная 20°C", color='royalblue', fontsize=9)

# 3. Анимируемые элементы
line, = ax.plot([], [], color='saddlebrown', lw=2.5, zorder=2)
dot, = ax.plot([], [], marker='o', markersize=9, color='crimson', zorder=3)
info_text = ax.text(0.7, 89, "", va='top', family='monospace', fontsize=10)

last_frame = len(t_anim) - 1

# 4. Функция обновления кадра
def update(frame):
    curr_t = t_anim[frame]
    curr_T = T_anim[frame]
    
    # Пройденный участок и позиция маркера
    line.set_data(t_anim[:frame+1], T_anim[:frame+1])
    dot.set_data([curr_t], [curr_T])
    
    # Плавная смена цвета от горячего красного к тёплому оранжевому/зелёному
    if curr_T > 65:
        dot.set_color('crimson')
    elif curr_T > 45:
        dot.set_color('darkorange')
    else:
        dot.set_color('seagreen')
        
    # Счётчик в левом верхнем углу
    info_text.set_text(f"t = {curr_t:4.1f} мин\nT = {curr_T:4.1f} °C")
    
    # Финальный кадр
    if frame == last_frame:
        dot.set_markersize(11)
        ax.set_title(f"Чай остыл до 40°C за {curr_t:.1f} мин!", fontsize=12, fontweight='bold', color='seagreen')
        
    return line, dot, info_text

# 5. Запуск анимации без зацикливания
ani = FuncAnimation(fig, update, frames=len(t_anim), interval=25, blit=False, repeat=False)

plt.tight_layout()
plt.show()
