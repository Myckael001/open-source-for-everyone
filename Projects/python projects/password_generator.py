import random
import string
import pyperclip

def generate_password(length=12, complexity='medium'):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    if complexity == 'low':
        all_chars = letters
    elif complexity == 'medium':
        all_chars = letters + digits
    elif complexity == 'high':
        all_chars = letters + digits + symbols
    else:
        all_chars = letters + digits

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password


def main():
    print("\n🔐 PASSWORD GENERATOR 🔐")
    print("-" * 30)

    try:
        length = int(input("Enter password length (e.g. 8, 12, 16): "))
    except ValueError:
        print("Invalid input! Using default length = 12.")
        length = 12

    print("\nChoose complexity level:")
    print("1. Low    (letters only)")
    print("2. Medium (letters + numbers)")
    print("3. High   (letters + numbers + symbols)")

    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        complexity = 'low'
    elif choice == '2':
        complexity = 'medium'
    elif choice == '3':
        complexity = 'high'
    else:
        complexity = 'medium'

    password = generate_password(length, complexity)
    print(f"\n✅ Your generated password:\n{password}")

    copy = input("\nCopy password to clipboard? (y/n): ").lower()
    if copy == 'y':
        pyperclip.copy(password)
        print("📋 Password copied to clipboard!")

    print("\nThanks for using the Password Generator! 🔑")


if __name__ == "__main__":
    main()
