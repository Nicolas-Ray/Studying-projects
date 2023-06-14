# Введение значения с валидацией, минус может быть только на 0 позиции, а точка на любой кроме 0 или -1

while True:
    user_input = input("Введите число: ")
    if (user_input.count('-') == 1 and user_input[0] == '-' and user_input.count('.') == 1 and '.' in user_input[1:-1]) or (user_input.count('-') == 1 and user_input[0] == '-' and user_input.count('.') == 0) or (user_input.count('.') == 1 and '.' in user_input[1:-1] and user_input.count('-') == 0) or (user_input.count('-') == 0 and user_input.count('.') == 0):
        break
    else:
        print("Неверный ввод.")

# Функция выбора множества
def setOfValue(value) :
    # Флаги для проверки
    isBool = False
    minus = False

    # Если на 0 позиции минус то число отрицательное
    if value[0] == "-":
            minus = True

    # Если присутствует точка, то число дробное
    if "." in value:
        isBool = True

    # Выбор типа множества в зависимотси от флага
    if isBool:
        # Рациональные
        set = "Q"
    elif not isBool and minus:
        # Целые
        set = "Z"
    else :
        # Натуральные
        set = "N"

    # Форма вывода
    return f"Set of {user_input} is {set}"

# Запуск функции
print(setOfValue(user_input))
