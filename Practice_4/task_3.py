def check_city(n):
    named_cities = set()

    for _ in range(n):
        city = input().strip()
        if city in named_cities:
            print("REPEAT")
            break
        else:
            print("OK")
            named_cities.add(city)


n = int(input("Играем в слова! Введите n число: "))

check_city(n)