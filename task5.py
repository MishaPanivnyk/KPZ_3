def point_location():
    x, y = map(float, input("Введіть координати точки A (x, y): ").split())

    if x == 0 and y == 0:
        print("Точка знаходиться в початку координат.")
    elif x == 0:
        print("Точка знаходиться на вісі Y.")
    elif y == 0:
        print("Точка знаходиться на вісі X.")
    elif x > 0 and y > 0:
        print("Точка знаходиться в першому квадранті.")
    elif x < 0 and y > 0:
        print("Точка знаходиться в другому квадранті.")
    elif x < 0 and y < 0:
        print("Точка знаходиться в третьому квадранті.")
    else:
        print("Точка знаходиться в четвертому квадранті.")

if __name__ == "__main__":
    point_location()
