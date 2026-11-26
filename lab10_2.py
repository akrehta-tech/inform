logs = {'INFO': 0, 'WARNING': 0, 'ERROR': 0, 'CRITICAL': 0}
for line in open('server_log.txt', encoding='utf-8'):
    line = line.rstrip('\n').split(maxsplit=3)
    logs[line[2]] = logs[line[2]] + 1
print(f'INFO: {logs.get("INFO", 0)}\nWARNING: {logs.get("WARNING", 0)}\nERRORS: {logs.get("ERROR", 0)}\nCRITICAL: {logs.get("CRITICAL", 0)}')
    

