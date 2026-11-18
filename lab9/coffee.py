import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Основные данные для графика (от 2 до 8 часов сна)
S = np.linspace(2, 8, 400)
C = 12 / S

# 2. Настройка фигуры, осей и стиля
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, 8.5)
ax.set_ylim(0, 7)

ax.set_title("Сколько кофе нужно, чтобы выжить", fontsize=12)
ax.set_xlabel("Часы сна S")
ax.set_ylabel("Чашки кофе C(S)")
ax.grid(True, alpha=0.3)

# Фоновая серая кривая (весь диапазон)
ax.plot(S, C, color='lightgray', lw=2, zorder=1)

# 3. Вертикальная асимптота при S = 0 и поясняющий текст
ax.axvline(0, ls='--', color='red', lw=1.5)
ax.text(0.15, 6.2, "S -> 0:\nкофе -> ∞", color='red', fontsize=10, fontweight='bold')

# 4. Отдельный массив для анимации (движение справа налево: от 8 до 2)
S_anim = np.linspace(8, 2, 300)
C_anim = 12 / S_anim

# Элементы, которые будут меняться в каждом кадре
brown_line, = ax.plot([], [], color='saddlebrown', lw=2.5, zorder=2)
marker, = ax.plot([], [], marker='o', markersize=10, color='green', zorder=3)
info_text = ax.text(4.8, 6.4, "", fontsize=11, family='monospace')

# Функция обновления каждого кадра
def update(frame):
    # Текущие координаты бегунка
    curr_s = S_anim[frame]
    curr_c = C_anim[frame]
    
    # Пройденный путь справа налево (коричневый след)
    brown_line.set_data(S_anim[:frame+1], C_anim[:frame+1])
    
    # Позиция маркера
    marker.set_data([curr_s], [curr_c])
    
    # Смена цвета маркера и иконки кружки в зависимости от часов сна
    if curr_s > 5.5:
        color = 'green'
        cup = '🍵'
    elif curr_s > 3.5:
        color = 'orange'
        cup = '☕'
    else:
        color = 'red'
        cup = '🔥'
        
    marker.set_color(color)
    
    # Обновление текста в правом верхнем углу
    info_text.set_text(f"сон = {curr_s:.1f} ч   кофе = {curr_c:.1f} {cup}")
    
    return brown_line, marker, info_text

# Запуск анимации
ani = FuncAnimation(fig, update, frames=len(S_anim), interval=30, blit=True)

plt.tight_layout()
plt.show()
