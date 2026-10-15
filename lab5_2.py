n = int(input())
for i in range(n):
    sp = ' ' * (n - i - 1)
    ht = '#' * (2 * i + 1)
    print(sp + ht)
print(' ' * (n - 1) + '#')