def count_negative_numbers():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))

    count = 0
    for num in [a, b, c]:
        if num < 0:
            count += 1

    print("Кількість негативних чисел:", count)

if __name__ == "__main__":
    count_negative_numbers()
