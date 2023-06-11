# Импортирую рандинт из рандом для генерции разных чисел в матрицы
from random import randint

# Первая матрица
matx_1 = [[randint(-10, 10), randint(-10, 10), randint(-10, 10)],
          [randint(-10, 10), randint(-10, 10), randint(-10, 10)],
          [randint(-10, 10), randint(-10, 10), randint(-10, 10)]]

# Вторая матрица
matx_2 = [[randint(-10, 10), randint(-10, 10), randint(-10, 10)],
          [randint(-10, 10), randint(-10, 10), randint(-10, 10)],
          [randint(-10, 10), randint(-10, 10), randint(-10, 10)]]

# Переменная для финальной матрицы
output_matx = []

#  Цикл по длинне как любая из матрицы так как для их сложения требуеться чтобы они были одинаковой длинны
for i in range(len(matx_1)):
  #  Создания переменной строки
    row = []
    # Длинная строки любой матрицы в цикле
    for j in range(len(matx_1[i])):
      # Добавление в строку сумму двух элиментов матрицы
        row.append(matx_1[i][j] + matx_2[i][j])
    # Вывод для наглядности
    print(row)
    #  Добавление строк в финальную матрицу
    output_matx.append(row)
    
# Вывод финальной матрицы
print(output_matx)
