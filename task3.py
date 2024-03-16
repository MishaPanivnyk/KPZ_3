def triangle_properties():
    angle1 = float(input("Введіть перший кут трикутника (в градусах): "))
    angle2 = float(input("Введіть другий кут трикутника (в градусах): "))

    angle3 = 180 - angle1 - angle2

    if angle1 > 0 and angle2 > 0 and angle3 > 0:
        print("Трикутник існує.")
        if angle1 == 90 or angle2 == 90 or angle3 == 90:
            print("Трикутник є прямокутним.")
        else:
            print("Трикутник не є прямокутним.")
    else:
        print("Трикутник не існує.")

if __name__ == "__main__":
    triangle_properties()
