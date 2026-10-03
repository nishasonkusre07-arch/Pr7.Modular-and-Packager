import math


def factorial():
    n = int(input("Enter a number: "))
    print("Factorial =", math.factorial(n))


def trigonometry():
    angle = float(input("Enter angle in degrees: "))
    rad = math.radians(angle)

    print("Sin =", math.sin(rad))
    print("Cos =", math.cos(rad))
    print("Tan =", math.tan(rad))


def logarithm():
    n = float(input("Enter number: "))
    print("Log =", math.log10(n))


def compound_interest():
    p = float(input("Principal Amount: "))
    r = float(input("Rate (%): "))
    t = float(input("Time (Years): "))

    amount = p * (1 + r / 100) ** t
    ci = amount - p

    print("Compound Interest =", round(ci, 2))
    print("Total Amount =", round(amount, 2))


def area_circle():
    r = float(input("Radius: "))
    area = math.pi * r * r
    print("Area =", round(area, 2))


def menu():
    while True:
        print("\n===== Mathematical Operations =====")
        print("1. Factorial")
        print("2. Trigonometry")
        print("3. Logarithm")
        print("4. Compound Interest")
        print("5. Area of Circle")
        print("6. Back")

        ch = input("Enter choice: ")

        if ch == "1":
            factorial()
        elif ch == "2":
            trigonometry()
        elif ch == "3":
            logarithm()
        elif ch == "4":
            compound_interest()
        elif ch == "5":
            area_circle()
        elif ch == "6":
            break
        else:
            print("Invalid Choice")
