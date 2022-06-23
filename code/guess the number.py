from random import *

print('Игра - Угадайка чисел')
num = randint(1, 100)
flag = False


def is_valid(number):
    if 101 > number > 0 and isinstance(number, int) == True:
        return True
    else:
        return False
    

while not flag:
    answer = int(input())
     if not is_valid(answer):
        print('Неверный тип данных или число в непраильном диапазоне!')
        continue
    if answer > num:
        print('Слишком много, попробуйте еще раз')
        continue
    elif answer < num:
        print('Слишком мало, попробуйте еще раз')
        continue
    elif answer == num:
        print('Вы угадали, поздравляем!')
        flag = True
