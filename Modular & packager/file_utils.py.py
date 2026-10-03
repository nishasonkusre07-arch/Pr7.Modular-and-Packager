def create_file():
    filename = input("Enter file name: ")

    with open(filename, "w") as f:
        text = input("Enter data: ")
        f.write(text)

    print("File created successfully.")


def read_file():
    filename = input("Enter file name: ")

    try:
        with open(filename, "r") as f:
            print("\nFile Content:")
            print(f.read())
    except FileNotFoundError:
        print("File not found.")


def append_file():
    filename = input("Enter file name: ")

    try:
        with open(filename, "a") as f:
            text = input("Enter data to append: ")
            f.write("\n" + text)

        print("Data appended successfully.")
    except FileNotFoundError:
        print("File not found.")


def menu():
    while True:
        print("\n===== File Operations =====")
        print("1. Create File")
        print("2. Read File")
        print("3. Append File")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            read_file()
        elif choice == "3":
            append_file()
        elif choice == "4":
            break
        else:
            print("Invalid Choice!")
