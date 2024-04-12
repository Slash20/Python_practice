# Задание 1

# def compres_string(string):
#     compressed_string = ""
#     count = 1
#     for i in range(len(string)-1):
#         if string[i] == string[i+1]:
#             count += 1
#         else:
#             if count > 1:
#                 compressed_string += string[i] + str(count)
#             else:
#                 compressed_string += string[i]
#             count = 1
#     if count > 1:
#         compressed_string += string[-1] + str(count)
#     else:
#         compressed_string += string[-1]
#     return compressed_string
#
# input_str = input()
# result = compres_string(input_str)
# print(result)



# Задание 2

# def decompress_string(compressed_string):
#     decompressed_string = ""
#     i = 0
#     while i < len(compressed_string):
#         char = compressed_string[i]
#         count = ""
#         i += 1
#         while i < len(compressed_string) and compressed_string[i].isdigit():
#             count += compressed_string[i]
#             i += 1
#         if count:
#             decompressed_string += int(count) * char
#         else:
#             decompressed_string += char
#     return decompressed_string
#
#
# compressed_str = input()
# result = decompress_string(compressed_str)
# print(result)




# Задание 3

# def number_to_words(number):
#     ones = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
#     teens = ["", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
#     tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
#     hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
#     thousand = ["тысяча"]
#
#
#     result = ""
#     if number > 999:
#         return thousand[0]
#     if number > 99:
#         result += hundreds[number // 100] + " "
#         number %= 100
#     if 10 <= number <= 19:
#         result += teens[number % 10] + " "
#     else:
#         result += tens[number // 10] + " "
#         result += ones[number % 10] + " "
#
#     return result.strip()
#
#
# number = int(input("Введите число от 1 до 1000: "))
# if number < 1 or number > 1000:
#     print("Вы вышли за пределы диапозона!")
# else:
#     print(number_to_words(number))


# Задание 4

# def count_arr(arr):
#     counts = []
#     for i in range(len(arr)):
#         count = 1
#         for j in range(i + 1, len(arr)):
#             if arr[i] == arr[j]:
#                 count += 1
#         if arr[i] not in counts:
#             counts.append(arr[i])
#             print(count, end=' ')
#
#
# arr1 = ["abc", "def", "ghi", "jkl", "abc", "def", "ghi", "jkl", "abc"]
# count_arr(arr1)

# Задание 5

# def check_liner_dep(matrix):
#     def gauss(matrix):
#         n = len(matrix)
#         for i in range(n):
#             if matrix[i][i] == 0:
#                 return False
#         for j in range(i+1, n):
#             coef = matrix[i][j] / matrix[i][i]
#             for k in range(n):
#                 matrix[j][k] -= coef*matrix[i][k]
#         return True
#
#     transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
#     return gauss(transposed_matrix)
#
# mat = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 80]
# ]
#
# result = check_liner_dep(mat)
#
# if result:
#     print("Столбцы матрицы являются линейно зависимыми")
# else:
#     print("Столбцы матрицы не являются линейно зависимыми")
#
# for row in mat:
#     print(row)


# Задание 6


# def create_abbreviation(pharse):
#     words = pharse.split()
#     abbreviation = ""
#     for word in words:
#         abbreviation += word[0].upper()
#     return abbreviation
#
#
# input_pharse = input("Введите строку: ")
# print(create_abbreviation(input_pharse))

