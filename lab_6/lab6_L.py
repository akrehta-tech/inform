inputText = input().split()
circle = list(range(1, int(inputText[0])+1))
k = int(inputText[1])
cou = 0
out = []
while len(circle) > 1:
    cou = (cou + k - 1) % len(circle)
    out.append(str(circle.pop(cou)))

last = circle[0]
print(f'{' '.join(out)} / {last}')

'''
1 2 3 4 5    /
1 3 4 5      / 2
1 3 5        / 2 4
3 5          / 2 4 1
3            / 2 4 1 5
'''