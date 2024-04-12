with open("input_3.txt", "r", encoding="utf-8") as file:
    children_data = file.readlines()

children = []
for line in children_data:
    surname, name, age = line.strip().split()
    children.append({"Фамилия": surname, "Имя": name, "возраст": int(age)})

oldest_child = max(children, key=lambda x: x["возраст"])
youngest_child = min(children, key=lambda x: x["возраст"])

with open("output_3_oldnes.txt", "w", encoding="utf-8") as file:
    file.write(f"{oldest_child['Фамилия']}") + file.write((f" {oldest_child['Имя']}")) + file.write(f" {oldest_child['возраст']}")

with open("output_3_young.txt", "w", encoding="utf-8") as file:
    file.write(f"{youngest_child['Фамилия']}") + file.write((f" {youngest_child['Имя']}")) + file.write(f" {youngest_child['возраст']}")
