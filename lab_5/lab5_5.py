import random
secret = random.randint(1,100)
while True:
    guess = int(input())
    if guess == secret:
        print('Угадал!')
        break
    if guess < secret:
        print('Больше')
    if guess > secret:
        print('Меньше')