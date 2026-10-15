depths = [1, 3, 2, 5, 4, 6, 1]
print('Исходник:', depths)
treas = []
for i in range(1, len(depths)-1):
    if depths[i] > depths[i-1] and depths[i] > depths[i+1]:
        treas.append(i)
treas_val = ', '.join([str(depths[ins]) for ins in treas])
print(f'Сокровища на индексах: {', '.join(str(x) for x in treas)} со значениями {treas_val}.')
if treas:
    total = max(depths[ix] for ix in treas)
    depths.remove(total)
print(f'Самое глубокое — {total}.')
print(f'Удаляем первое вхождение числа {total} из списка:')
print(f'{depths} — это и есть ответ')
