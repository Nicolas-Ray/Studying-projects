from random import *

print('Игра - Угадайка чисел')
num = randint(1, 100)
flag = False

while not flag:
    answer = int(input())
    if answer > num:
        print('Слишком много, попробуйте еще раз')
        continue
    elif answer < num:
        print('Слишком мало, попробуйте еще раз')
        continue
    elif answer == num:
        print('Вы угадали, поздравляем!')
        flag = True
