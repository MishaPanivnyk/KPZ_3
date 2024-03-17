def replace_numbers():
    a = int(input("Введіть число a: "))
    b = int(input("Введіть число b: "))

    if a != b:
        max_num = max(a, b)
        a = b = max_num
    else:
        a = b = 0

    print("Нові значення:", a, b)

if __name__ == "__main__":
    replace_numbers()
