import numpy as np

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])

zeros = np.where(x == 0)[0]  # находим индексы нулевых элементов
max_after_zero = 0

for index in zeros:
    if index < len(x) - 1: # проверяем, что индекс не последний
        max_after_zero = max(max_after_zero, x[index + 1]) # находим максимальный элемент, следующий за нулевым

print(max_after_zero)
