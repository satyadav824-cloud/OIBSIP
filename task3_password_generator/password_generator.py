import random
import string

print("=" * 50)
print("      RANDOM PASSWORD GENERATOR")
print("=" * 50)

while True:
    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("❌ Password length should be at least 4.")
            continue

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = "".join(random.choice(characters) for _ in range(length))

        print("\n✅ Your Generated Password:")
        print(password)
        if length < 8:
            print("password strength: Weak")

        elif length<12:
            print("password strength: Moderate")
        else:
            print("password strength: Strong")
    except ValueError:
        print("❌ Please enter a valid number.")

    choice = input("\nGenerate another password? (yes/no): ").lower()

    if choice != "yes":
        print("\nThank you for using Password Generator 😊")
        break