# Задание 1

# def count_uniq_numbers(numbers):
#     uniq_numbers = set(numbers)
#     return len(uniq_numbers)
#
#
# input_numbers = input("Введите какие-нибудь целые числа: ")
# numbers_list = [int(num.strip()) for num in input_numbers.split(',')]
# uniq_count = count_uniq_numbers(numbers_list)
# print(uniq_count)


# Задание 2

# def is_subset(set1, set2):
#     if set1 == set2: return False
#     return set1.issubset(set2)
#
#
# set1 = {1, 2, 3, 4, 5, 6, 7}
# set2 = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0}
#
# print(is_subset(set1, set2))


# Задача 3

# def check_city(n):
#     named_cities = set()
#
#     for _ in range(n):
#         city = input().strip()
#         if city in named_cities:
#             print("REPEAT")
#             break
#         else:
#             print("OK")
#             named_cities.add(city)
#
#
# n = int(input("Играем в слова! Введите n число: "))
#
# check_city(n)


# Задание 4

# def count_word_occurrences(text):
#     word_count = {}
#     words = text.split()
#
#     for word in words:
#         if word in word_count:
#             print(word_count[word], end=" ")
#         else:
#             print("0", end=" ")
#         word_count[word] = word_count.get(word, 0) + 1
#
#
# input_text = input("Enter the text: ")

# count_word_occurrences(input_text)


# Задание 5

# def display_shopping_list(purchase_records):
#     for customer_id, purchases in purchase_records.items():
#         print("Customer ID:", customer_id)
#         print("Shopping List:")
#         for product, quantity in purchases:
#             print(f"{product}: {quantity}")
#         print()
#
#
# n = int(input("Enter the number of purchase records: "))
# purchase_records = {}
#
# for _ in range(n):
#     record = input("Enter purchase record (CustomerID Product Quantity): ").split()
#     customer_id = int(record[0])
#     product = record[1]
#     quantity = int(record[2])
#
#     if customer_id in purchase_records:
#         purchase_records[customer_id].append((product, quantity))
#     else:
#         purchase_records[customer_id] = [(product, quantity)]
#
#
# display_shopping_list(purchase_records)


# 6 задание

# def count_words(text):
#     word_counts = {}
#     for word in text.lower().split():
#         word_counts[word] = word_counts.get(word, 0) + 1
#     print(word_counts)
#     return word_counts
#
#
# def sort_key(item):
#     return -item[1], item[0]
#
#
# text = input()
# word_counts = count_words(text)
# sorted_words = sorted(word_counts.items(), key=sort_key)
# for word, count in sorted_words:
#     print(word)

