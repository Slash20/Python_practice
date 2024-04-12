
# Задача 1
# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
# c = int(input("Введите число c: "))
#
#
# if a == b == c:
#     print("Сопадают 3 числа")
# elif a == b and b != c:
#     print("Сопадают 2 числа")
# else:
#     print("Все числа различны")



# Задача 2
# n = int(input("Введите число лесенок: "))
#
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end='')
#     print()


# Задача 3

n = int(input("Введите число ступенек n: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i+1):
        print(j, end="")
    print()

