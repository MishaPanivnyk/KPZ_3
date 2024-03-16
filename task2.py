def calculate_distance():
    x1, y1 = map(float, input("Введіть координати точки A (x1, y1): ").split())
    x2, y2 = map(float, input("Введіть координати точки B (x2, y2): ").split())

    distance_a = (x1 ** 2 + y1 ** 2) ** 0.5
    distance_b = (x2 ** 2 + y2 ** 2) ** 0.5

    if distance_a < distance_b:
        print("Точка A знаходиться ближче до початку координат.")
    elif distance_b < distance_a:
        print("Точка B знаходиться ближче до початку координат.")
    else:
        print("Точки знаходяться на однаковій відстані до початку координат.")

if __name__ == "__main__":
    calculate_distance()
