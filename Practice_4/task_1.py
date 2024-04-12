def count_uniq_numbers(numbers):
    uniq_numbers = set(numbers)
    return len(uniq_numbers)


input_numbers = input("Введите какие-нибудь целые числа: ")
numbers_list = [int(num.strip()) for num in input_numbers.split(',')]
uniq_count = count_uniq_numbers(numbers_list)
print(uniq_count)