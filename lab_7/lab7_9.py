n, m = map(int, input().split())
A = [[0] * m for _ in range(n)]
for j in range(m):
    A[0][j] = 1
for i in range(n):
    A[i][0] = 1
for i in range(1, n):
    for j in range(1, m):
        A[i][j] = A[i - 1][j] + A[i][j - 1]
for row in A:
    print("".join(f"{x:6d}" for x in row))
