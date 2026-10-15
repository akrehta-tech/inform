print(sum([x[1]-x[0] >= 2 for x in [list(map(int, x.strip().split())) for x in input().split('/')][1:]]))
