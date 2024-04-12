def display_shopping_list(purchase_records):
    for customer_id, purchases in purchase_records.items():
        print("Customer ID:", customer_id)
        print("Shopping List:")
        for product, quantity in purchases:
            print(f"{product}: {quantity}")
        print()


n = int(input("Введите число: "))
purchase_records = {}

for _ in range(n):
    record = input("Enter purchase record (CustomerID Product Quantity): ").split()
    customer_id = int(record[0])
    product = record[1]
    quantity = int(record[2])

    if customer_id in purchase_records:
        purchase_records[customer_id].append((product, quantity))
    else:
        purchase_records[customer_id] = [(product, quantity)]


display_shopping_list(purchase_records)