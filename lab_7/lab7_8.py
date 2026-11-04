n, m = map(int, input().split())
hall = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
result = 0
for i in range(n):
    count = 0
    found = False
    for j in range(m):
        if hall[i][j] == 0:
            count += 1
            if count >= k:
                found = True
                break
        else:
            count = 0
    if found:
        result = i + 1
        break

print(result)
