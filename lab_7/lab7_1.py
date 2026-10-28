#метод прямоугольников
parts = [10, 100, 1000, 10000]
left_border, right_border = -2, 5

def Counter(x):
    return x ** 2 / 10 + 1


for part in parts:
    integral = 0
    h = (right_border - left_border) / part
    for i in range(part):
        x_i = left_border + i * h
        integral += Counter(x_i) * h
    print(f'N={part}: {integral:.2f}')
