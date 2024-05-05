import numpy as np


def run_length_encoding(x):
    unique_values, counts = np.unique(x, return_counts=True)

    # Преобразуем результаты в обычные списки
    unique_values = list(unique_values)
    counts = list(counts)

    # Создаем кортеж для возврата результата
    result = (unique_values, counts)

    return result


# Пример использования функции
x = np.array([1, 2, 2, 3, 3, 3, 3, 5, 5, 5])
print(run_length_encoding(x))
