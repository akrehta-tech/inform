import numpy as np
import matplotlib.pyplot as plt


names = ["Маргарита Мания", "Пепперони-Парад", "Гавайский Хаос",
         "Четыре Сыра и Слёзы", "Веганский Бунт"]
sales = [23, 45, 56, 78, 32]


x = np.arange(len(names))


winner_idx = np.argmax(sales)
winner_name = names[winner_idx]
winner_sales = sales[winner_idx]
print(f"Победитель: {winner_name} — {winner_sales} пицц")


fig, ax = plt.subplots(figsize=(10, 5))


colors = ['steelblue'] * len(names)
colors[winner_idx] = 'crimson'
edges = ['navy'] * len(names)
edges[winner_idx] = 'darkred'
linewidths = [1.2] * len(names)
linewidths[winner_idx] = 2.5

bars = ax.bar(x, sales, width=0.6, color=colors, edgecolor=edges, linewidth=linewidths, zorder=3)

for i, (bar, value) in enumerate(zip(bars, sales)):
    ax.text(bar.get_x() + bar.get_width() / 2, value + 1.5, str(value), ha='center', va='bottom', fontsize=11, fontweight='bold' if i == winner_idx else 'normal', color='crimson' if i == winner_idx else 'black')


ax.set_title("Битва пиццерий: продажи за неделю", fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel("Пиццерия", fontsize=12)
ax.set_ylabel("Продано пицц, шт.", fontsize=12)

ax.set_xticks(x)
ax.set_xticklabels(names, rotation=15, ha='right', fontsize=10)


ax.grid(axis='y', linestyle='--', alpha=0.6, zorder=0)
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_ylim(0, max(sales) * 1.15)


ax.annotate('Победитель!', xy=(winner_idx, winner_sales),
            xytext=(winner_idx, winner_sales + 14),
            ha='center', fontsize=11, color='crimson',
            fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='crimson', lw=1.5))

plt.tight_layout()
plt.savefig('pizzeria.png', dpi=150)

plt.show()
