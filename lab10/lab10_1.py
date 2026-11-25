writing = open("errors_only.txt", "w+")
for line in open("server_log.txt", "r", encoding="utf-8"):
    if line.find('CRITICAL') != -1 or line.find('ERROR') != -1:
        writing.write(line)
writing.close()
with open('errors_only.txt', encoding="utf-8") as f:
    line_count = sum(1 for _ in f)
print(f'Найдено {line_count} критических ошибок')

