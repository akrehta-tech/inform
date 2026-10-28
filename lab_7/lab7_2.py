#метод трапеций
parts = [10, 100, 1000]
left_border, right_border = -2, 5

def Counter(x):
    return x ** 2 / 10 + 1


for part in parts:
    h = (right_border - left_border) / part
    f0 = Counter(left_border)
    f_lt = Counter(right_border)
    integral = (h/2) * (f0 + f_lt)
    for i in range(part):
        x_i = left_border + i * h
        integral += Counter(x_i) * h
    print(f'N={part}: {integral:.2f}')
