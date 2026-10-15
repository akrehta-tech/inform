digits = [int(x) for x in input()]
result = sum(digits[1::2])
result += sum([x - 9 if x > 9 else x for x in [y*2 for y in digits[::2]]]) #[8, 5, 8, 0, 2, 6, 2, 2]
if result % 10 == 0:
    print('Корректный номер')
else:
    print('Некорректный номер')
#_________
digits = [int(x) for x in input()]
print('Корректный номер' if (sum(digits[1::2]) + sum([x - 9 if x > 9 else x for x in [y*2 for y in digits[::2]]])) % 10 == 0 else 'Некорректный номер')
