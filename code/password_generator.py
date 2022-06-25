
from random import choice

digits = '0123456789'
low = 'abcdefghijklmnopqrstuvwxyz'
upp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punc = '!#$%&*+-=?@^_'
chars = ''

pas_amount = int(input('Введите количество паролей - '))
pas_len = int(input('Введите длинну пароля - '))

digits_in = input('Цифры в пароле да/нет - ')
low_in = input('Маленькие буквы в пароле да/нет - ')
upp_in = input('Большие буквы в пароле да/нет - ')
punc_in = input('Символы в пароле да/нет - ')
not_in = input('Исключать ли неоднозначные символы il1Lo0O? да/нет - ')

if digits_in == 'да' or digits_in == 'Да':
    chars += digits
if low_in == 'да' or low_in == 'Да':
    chars += low
if upp_in == 'да' or upp_in == 'Да':
    chars += upp
if punc_in == 'да' or punc_in == 'Да':
    chars += punc
if not_in == 'да' or not_in == 'Да':
    for i in 'il1Lo0O':
        chars.replace(i, '')


def gen_pas(x, y):
    password = ''
    for _ in range(x):
        password += choice(chars)
    print()
    print(password)


for _ in range(pas_amount):
    gen_pas(pas_len, chars)

    
    
