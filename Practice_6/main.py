import csv
import os
import random


def load_csv(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data


def show(data, output_type='top', num_rows=5, separator=','):
    if output_type == 'bottom':
        data_to_show = data[-num_rows:]
    elif output_type == 'random':
        data_to_show = random.sample(data, num_rows)
    else:
        data_to_show = data[:num_rows]

    for row in data_to_show:
        print(separator.join(row.values()))


def info(data):
    header = data[0]
    num_rows = len(data) - 1
    num_cols = len(header)
    print(f"Number of rows x columns: {num_rows}x{num_cols}")

    print("Field Name\tQty\tType")
    for field in header:
        non_empty_count = sum(1 for row in data[1:] if row[field])
        field_type = type(data[1][field]).__name__
        print(f"{field}\t{non_empty_count}\t{field_type}")


def del_nan(data):
    return [row for row in data if all(row.values())]


def make_ds(data):
    learning_data = random.sample(data, int(0.7 * len(data)))
    testing_data = [row for row in data if row not in learning_data]

    os.makedirs("workdata/Learning", exist_ok=True)
    os.makedirs("workdata/Testing", exist_ok=True)

    with open("workdata/Learning/train.csv", 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(learning_data)

    with open("workdata/Testing/test.csv", 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(testing_data)


filename = "Titanic.csv"
data = load_csv(filename)
show(data, output_type='top', num_rows=5)

info(data)
data = del_nan(data)
make_ds(data)
