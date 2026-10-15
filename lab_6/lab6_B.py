s = input().split()
rez = []
for i in range(1, len(s)):
    if s[i] > s[i-1]:
        rez.append(s[i])
print(' '.join(rez))
