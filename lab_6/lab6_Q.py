inputText = [x.strip().split() for x in input().split('/')]
x = inputText[1].count('R') - inputText[1].count('L')
y = inputText[1].count('U') - inputText[1].count('D')
print(f'{x} {y} / {abs(x) + abs(y)}')
