email = input("Email: ")
if email.count('@') != 1:
    print("x должен содержать ровно одну '@'")
if email[0] in '@.' or email[-1] in '@.':
    print("x не должен начинаться с . или @")
if len(email) < 6 or len(email) > 30:
    print("x длина должна быть от 6 до 30 символов")
if not ('@' in email and '.' in email.split('@', 1)[-1]):
    print("x нет . после @")
else:
    print('OK')

password = input("Пароль: ")
if len(password) < 8:
    print("x слишком короткий")
if not any(c.isdigit() for c in password):
    print("x нет цифры")
if not any(x for x in password if x.isupper() and x.isascii()):
    print("x нет заглавной буквы")
if not any(x for x in password if x in '!@#$%^&*'):
    print("x нет спецсимвола")
else:
    print('')