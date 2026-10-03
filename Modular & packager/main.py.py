from utils import datetime_utils
from utils import math_utils
from utils import random_utils
from utils import uuid_utils
from utils import file_utils
import math


def explore_modules():
    print("\n===== Module Attributes =====")
    print("\nMath Module:")
    print(dir(math))

    print("\nCustom Module (math_utils):")
    print(dir(math_utils))


def datetime_menu():
    while True:
        print("\n===== Date & Time Operations =====")
        print("1. Current Date & Time")
        print("2. Date Difference")
        print("3. Custom Date Format")
        print("4. Stopwatch")
        print("5. Countdown")
        print("6. Back")

        ch = input("Enter your choice: ")

        if ch == "1":
            datetime_utils.current_datetime()
        elif ch == "2":
            datetime_utils.date_difference()
        elif ch == "3":
            datetime_utils.custom_format()
        elif ch == "4":
            datetime_utils.stopwatch()
        elif ch == "5":
            datetime_utils.countdown()
        elif ch == "6":
            break
        else:
            print("Invalid Choice!")


def main():
    while True:
        print("\n==============================")
        print(" Welcome to Multi-Utility Toolkit ")
        print("==============================")
        print("1. Date & Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. UUID Generation")
        print("5. File Operations")
        print("6. Explore Module Attributes")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_utils.menu()
        elif choice == "3":
            random_utils.menu()
        elif choice == "4":
            uuid_utils.menu()
        elif choice == "5":
            file_utils.menu()
        elif choice == "6":
            explore_modules()
        elif choice == "7":
            print("\nThank you for using the Multi-Utility Toolkit!")
            break
        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()
