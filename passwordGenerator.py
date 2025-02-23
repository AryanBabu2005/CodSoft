import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def main():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 4:
                print("Password length should be at least 4 characters.")
                continue
            password = generate_password(length)
            print(f"Generated Password: {password}")
        except ValueError:
            print("Please enter a valid number.")

        another = input("Do you want to generate another password? (yes/no): ").lower()
        if another != "yes":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
