line1 = input()
line2 = input()
line3 = input()
counter_i = 0
counter_j = 0
counter_k = 0
if line1 == "" or line2 == "" or line3 == "":
    print('Не хайку. Должно быть 3 строки.')
else:
    for i in line1.lower():
        if i in 'аеёиоуыэюя':
            counter_i += 1


    for j in line2.lower():
        if j in 'аеёиоуыэюя':
            counter_j += 1


    for k in line3.lower():
        if k in 'аеёиоуыэюя':
            counter_k += 1


    if counter_i == counter_k == 5 and counter_j == 7:
        print('Хайку!')
    else:
        print('Не хайку.')