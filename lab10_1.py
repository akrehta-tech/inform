to_wrt = open('errors_only.txt', 'w+')
for line in open('server_log.txt', encoding='utf-8'):
    if line.find('ERROR') != -1 or line.find('CRITICAL') != -1:
        to_wrt.write(line)
to_wrt.close()
with open('errors_only.txt', encoding="utf-8") as f:
    line_count = sum(1 for _ in f)
print(f'Найдено {line_count} критических ошибок')