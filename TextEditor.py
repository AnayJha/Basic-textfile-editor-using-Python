def write_to_file():
    filename = input("Enter filename: ")
    content = input("Enter content: ")
    with open(filename, 'w') as f:
        f.write(content)
    print("Content written to file successfully!")
    print("---------------")

def read_from_file():
    filename = input("Enter filename: ")
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print("File content:\n", content)
    except FileNotFoundError:
        print("File not found!")
        print("---------------")

def main():
    while True:
        choice = input("Choose (1) Write, (2) Read, (3) Exit: ")
        if choice == '1':
            write_to_file()
        elif choice == '2':
            read_from_file()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()