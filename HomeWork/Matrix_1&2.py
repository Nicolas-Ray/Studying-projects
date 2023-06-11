# ЗАДАНИЕ - 1

# Входные данные
m = int(input('Enter M:'))
n = int(input('Enter N:'))

# Функция для создания матрицы
def make_matrix(m, n):
    # Пустая матрица
    matrix = []
    for i in range(m):
        # Создания пустой строки
        row = []
        for j in range(n):
            # Добавление элементов в строку
            row.append(0)
        # Печать для наглядного вида матрицы
        print(row)
        # Добавление строки в патрицу
        matrix.append(row)
    return matrix

# Создание матрицы
outputMatrix = make_matrix(m, n)

# Вывод матрицы
print(outputMatrix)


# ЗАДАНИЕ - 2

# Входные данные
m = int(input('Enter M:'))
n = int(input('Enter N:'))

# Функция для создания матрицы
def make_matrix(m, n):
    # Пустая матрица
    matrix = []
    for i in range(m):
        # Создания пустой строки
        row = []
        for j in range(n):
            # Добавление кастомного элимента
            el = int(input('Add element:'))
            # Добавление элементов в строку
            row.append(el)
        # Печать для наглядного вида матрицы
        print(row)
        # Добавление строки в патрицу
        matrix.append(row)
    return matrix

# Создание матрицы
outputMatrix = make_matrix(m, n)

# Вывод матрицы
print(outputMatrix)
