import random as ran
rez = [ran.choice(['О', 'Р']), ran.choice(['О', 'Р']), ran.choice(['О', 'Р'])]
while True:
    if rez[-1] == rez[-2] == rez[-3]:
        break
    else:
        rez.append(ran.choice(['О', 'Р']))
print(rez, len(rez))
rez_n = ' '.join(rez)
print(f'{rez_n} (попыток: {len(rez)})')