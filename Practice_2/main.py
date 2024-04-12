# Задание 1

# n = int(input("Введите число n строк: "))
#
# list = []
#
# for i in range(n):
#     row = [1] * (i + 1)
#     for j in range(i + 1):
#         if j != 0 and j != i:
#             row[j] = list[i - 1][j - 1] + list[i - 1][j]
#     list.append(row)
#
# for r in list:
#     print(r)


# Задание 2
value = int(2 ** float(input("Введите число большее 2-х: ")))

triangle = [[0] * value for _ in range(value)]

for i in range(value):
    triangle[i][0] = 1
    triangle[i][i] = 1

for i in range(1, value):
    for j in range(1, value):
        triangle[i][j] = (triangle[i - 1][j - 1] + triangle[i - 1][j]) % 2

for i, row in enumerate(triangle):
    spaces = " " * (value - i - 1)
    print(f"{spaces}{' '.join(['*' if cell == 1 else ' ' for cell in row]).strip()}")
