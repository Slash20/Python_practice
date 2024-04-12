with open("input_1.txt", "r") as file:
    count = 1
    for line in file:
        numbers = list(map(int, line.split()))
        for number in numbers:
            count *= number

with open("output_1.txt", "w") as file:
    file.write(str(count))
