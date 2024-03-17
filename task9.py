def count_integer_numbers():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))

    count = 0
    for num in [a, b, c]:
        if num.is_integer():
            count += 1

    print("Кількість цілих чисел:", count)

if __name__ == "__main__":
    count_integer_numbers()
