import numpy as np

# Генерация массива случайных чисел нормального распределения размера 10x4
array = np.random.randn(10, 4)

# Вычисление минимальных, максимальных, средних значений и стандартного отклонения
min_value = array.min()
max_value = array.max()
mean_value = array.mean()
std_deviation = array.std()

# Сохранение первых 5 строк в отдельную переменную
first_five_rows = array[:5]

print("Минимальное значение:", min_value)
print("Максимальное значение:", max_value)
print("Среднее значение:", mean_value)
print("Стандартное отклонение:", std_deviation)
print("Первые пять строк:")
print(first_five_rows)
