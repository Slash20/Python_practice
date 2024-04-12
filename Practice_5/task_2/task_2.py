with open("input_2.txt", 'r', encoding='utf-8') as file:
    data = [int(i) for i in file.readlines()]

with open("output_2.txt", 'w', encoding='utf-8') as file:
    file.writelines(str(i) + '\n' for i in sorted(data))