def main():
    password = input("Enter a password")
    while len(password) < 5:
        password = input("Enter a password")
    print("*" * len(password))


main()
