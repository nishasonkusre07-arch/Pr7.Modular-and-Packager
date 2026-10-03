import uuid


def generate_uuid():
    uid = uuid.uuid4()
    print("\nGenerated UUID:")
    print(uid)


def menu():
    while True:
        print("\n===== UUID Operations =====")
        print("1. Generate UUID")
        print("2. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_uuid()
        elif choice == "2":
            break
        else:
            print("Invalid Choice!")
