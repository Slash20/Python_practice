import json
import csv
import os
import sys


def json_to_csv(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    root_record = list(data.keys())[0]
    csv_filename = os.path.splitext(json_file)[0] + '.csv'

    headers = list(data[root_record][0].keys())

    with open(csv_filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data[root_record])

    print(f"CSV файл '{csv_filename}' создан.")



if len(sys.argv) != 2:
    print("Используйте команду: python <filename>.py <json_file>")
    sys.exit(1)

json_file = sys.argv[1]
if not os.path.isfile(json_file):
    print(f"Ошибка: файл '{json_file}' не найден.")
    sys.exit(1)

json_to_csv(json_file)
