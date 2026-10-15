arm = 0
n = int(input())

for i in range(1, n + 1):
    c = list(str(i))
    f = sum([int(x) ** len(c) for x in c])
    arm += (i == f)
print(arm)