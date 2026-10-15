inputText = [x.strip() for x in input().split('/')][1:]
print(' / '.join([x[0]+ str(len(x) - 2) + x[-1] if len(x) > 10 else x for x in inputText]))

