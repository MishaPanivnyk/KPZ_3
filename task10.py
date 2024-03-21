def find_divisor():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))
    k = float(input("Введіть число k: "))

    divisors = []
    if a % k == 0:
        divisors.append('a')
    if b % k == 0:
        divisors.append('b')
    if c % k == 0:
        divisors.append('c')

    if divisors:
        print(f"Число {k} є дільником чисел: {', '.join(divisors)}")
    else:
        print(f"Число {k} не є дільником жодного з чисел.")

if __name__ == "__main__":
    find_divisor()
