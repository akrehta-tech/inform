'''
Напишите программу, которая будет случайным образом генерировать лотерейный билет — то есть шесть уникальных чисел в диапазоне от 1 до 49.
'''

import random
res = []
for i in range(6):
    s = str(random.randint(1, 49))
    if s not in res:
        res.append(s)
print(" ".join(res))
