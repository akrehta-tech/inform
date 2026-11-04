import matplotlib.pyplot as plt


labels = ["Спасает мир", "Сон (восстановление сил)",
          "Кибер-квесты", "Другое"]
hours = [8, 7, 5, 4]


fig, ax = plt.subplots(figsize=(7, 7))


colors = ['crimson', 'royalblue', 'seagreen', 'goldenrod']
explode = [0.05, 0, 0, 0]

wedges, texts, autotexts = ax.pie(
    hours,
    labels=labels,
    autopct='%1.1f%%',
    colors=colors,
    explode=explode,
    startangle=90,
    counterclock=False,
    wedgeprops=dict(edgecolor='white', linewidth=1.5),
    textprops=dict(fontsize=11)
)


for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(12)


ax.set_title("День супергероя Алексея",
             fontsize=16, fontweight='bold', pad=20)

ax.axis('equal')

plt.tight_layout()


plt.savefig('superhero.png', dpi=150)

plt.show()
