inputText = [x.strip().split() for x in input().split('/')]
g = int(inputText[0][1]) % int(inputText[0][0])
print(' '.join(inputText[1][-g:] + inputText[1][:-g]))
