import random
import string


def random_number():
    print("Random Number:", random.randint(1, 100))


def random_list():
    data = [10, 20, 30, 40, 50]
    random.shuffle(data)
    print("Shuffled List:", data)


def random_password():
    chars = string.ascii_letters + string.digits + "@#$%&"
    password = "".join(random.choice(chars) for _ in range(8))
    print("Password:", password)


def otp():
    print("OTP:", random.randint(100000, 999999))


def sampling():
    data = [1,2,3,4,5,6,7,8,9,10]
    print("Sample:", random.sample(data, 3))


def menu():
    while True:
        print("\n===== Random Operations =====")
        print("1. Random Number")
        print("2. Shuffle List")
        print("3. Random Password")
        print("4. OTP")
        print("5. Random Sample")
        print("6. Back")

        ch = input("Enter choice: ")

        if ch == "1":
            random_number()
        elif ch == "2":
            random_list()
        elif ch == "3":
            random_password()
        elif ch == "4":
            otp()
        elif ch == "5":
            sampling()
        elif ch == "6":
            break
        else:
            print("Invalid Choice")
