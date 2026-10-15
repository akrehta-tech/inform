inp = input().split()
x = int(inp[0])
heights = inp[2:]
pos = 1
for h in heights:
    if int(h) >= x:
        pos += 1
    else:
        break
print(pos)