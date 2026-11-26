dict_lines = {}
for line in open('olimp.txt', encoding='utf-8'):
    line = line.rsplit(maxsplit=1)
    dict_lines[line[0]] = line[1]
sorted_dict = dict(sorted(dict_lines.items(), key=lambda it: int(it[1]), reverse=True))
key, item = list(sorted_dict.items())[1]
print(f'{key}: {item}')
