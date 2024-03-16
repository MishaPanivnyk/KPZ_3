def calculate_power():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    c = float(input("Введіть третє число: "))

    result = []
    for num in [a, b, c]:
        if num >= 0:
            result.append(num ** 2)
        else:
            result.append(num ** 4)

    print("Результат:", result)

if __name__ == "__main__":
    calculate_power()
