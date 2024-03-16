def replace_numbers():
    x = float(input("Введіть перше число x: "))
    y = float(input("Введіть друге число y: "))

    if x != y:
        x_new = max(x, y)
        y_new = min(x, y) / 2
    else:
        x_new = y_new = 0

    print("Нові значення:", x_new, y_new)

if __name__ == "__main__":
    replace_numbers()
