
from random import randint

print('Игра - Угадайка чисел')


def is_valid(number):
    if 101 > number > 0 and isinstance(number, int) == True:
        return True
    else:
        return False


def game(num, flag, counter):
    while not flag:
        answer = int(input('Ваш ответ - '))
        if not is_valid(answer):
            print('Неверный тип данных или число в непраильном диапазоне!')
            counter += 1
            continue
        if answer > num:
            print('Слишком много, попробуйте еще раз')
            counter += 1
            continue
        elif answer < num:
            print('Слишком мало, попробуйте еще раз')
            counter += 1
            continue
        elif answer == num:
            print('Вы угадали, поздравляем!')
            print()
            print(f'Вам потребовалось {counter} попыток. ')
            flag = True
    print()
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')


n = int(input('Введите диапазон - '))
num = randint(1, n)
flag = False
counter = 0

game(num, flag, counter)

restart = input('Хотите начать заново? Да/Нет - ')

if restart == 'Да' or restart == 'да':
    n = int(input('Введите диапазон - '))
    num = randint(1, n)
    flag = False
    counter = 0
    game(num, flag, counter)
elif restart == 'Нет' or restart == 'нет':
    exit(0)
else:
    print('Неверное значение, попробуйте еще раз.')
restart = input('Хотите начать заново? Да/Нет - ')

