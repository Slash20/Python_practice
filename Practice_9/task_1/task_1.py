text = "Сохранить этот текст в файл. Прочитать матрицу из файла. Hайдите для этой матрицы сумму всех элементов, максимальный и минимальный элемент (число)\n3,4,17,-3\n5,11,-1,6\n0,2,-5,8"
with open('matrix_task.txt', 'w') as file:
    file.write(text)

# Читаем матрицу из файла
with open('matrix_task.txt', 'r') as file:
    lines = file.readlines()[1:]  # Пропускаем первую строку

matrix = [list(map(int, line.strip().split(','))) for line in lines]  # Преобразуем строки в матрицу чисел


sum_of_elements = sum(sum(row) for row in matrix)
max_element = max(map(max, matrix))
min_element = min(map(min, matrix))


print("Матрица:")
for row in matrix:
    print(row)
print("Сумма всех элементов:", sum_of_elements)
print("Максимальный элемент:", max_element)
print("Минимальный элемент:", min_element)
