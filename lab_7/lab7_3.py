import random
n = 3
magic = [[0] * n for _ in range(n)]
i, j = 0, n // 2
for num in range(1, n * n + 1):
    magic[i][j] = num
print(magic[0])
