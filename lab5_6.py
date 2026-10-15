message = input("Введите сообщение: ")
menuItem = {
    0: {"text" : "\b\b\b", "func" : lambda x: "Ошибка ввода действия"},
    1: {"text" : "Проверка на палиндром (без учёта регистра и пробелов).", "func" : lambda x: (''.join(ch.lower() for ch in x if ch.isalnum())) == (''.join(ch.lower() for ch in x if ch.isalnum()))[::-1]},
    2: {"text" : "Подсчёт гласных (a, e, i, o, u).", "func" : lambda x: sum(1 for char in x.lower() if char in "аеёиоуыэюяaeiou")},
    3: {"text" : "Проверка «только цифры»", "func" : lambda x: x.isdigit()},
    4: {"text" : "Проверка «только буквы»", "func" : lambda x: x.isalpha()},
    5: {"text" : "Переворот строки", "func" : lambda x: x[::-1]},
    6: {"text" : "Верхний регистр", "func" : lambda x: x.upper()},
    7: {"text" : "Нижний регистр", "func" : lambda x: x.lower()},
    8: {"text" : "Замена пробелов на _", "func" : lambda x: x.replace("_", " ")},
    9: {"text" : "Проверка на email", "func" : lambda x: '@' in x and '.' in x.split('@', 1)[-1]},
    10: {"text" : "Извлечение домена", "func" : lambda x: x.split('@', 1)[-1] if '@' in x else "Domain not found"},
    11: {"text" : "Выход.", "func" : lambda x: "Всего хорошеГо"}
}
inputAction = 0
while inputAction != 11:
    for key, menuString in menuItem.items():
        print(f"{key}. {menuString['text']}")
    inputAction = int(input("Выберите действие (1–11):"))
    if inputAction < 1 or inputAction > 11:
        inputAction = 0
    print((menuItem[inputAction]["func"])(message))
    
