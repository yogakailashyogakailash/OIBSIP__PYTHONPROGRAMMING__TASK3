# ----------------------------------------
#     RANDOM PASSWORD GENERATOR
# ----------------------------------------

import random
import string

def generate_password():

    print("===== RANDOM PASSWORD GENERATOR =====")

    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("❌ Length must be greater than 0.")
            return

        print("\nSelect character types:")
        print("1. Letters")
        print("2. Numbers")
        print("3. Symbols")
        print("4. Letters + Numbers")
        print("5. Letters + Numbers + Symbols")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            characters = string.ascii_letters
        elif choice == "2":
            characters = string.digits
        elif choice == "3":
            characters = string.punctuation
        elif choice == "4":
            characters = string.ascii_letters + string.digits
        elif choice == "5":
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            print("❌ Invalid choice.")
            return

        password = ""
        for i in range(length):
            password += random.choice(characters)

        print("\n✅ Generated Password:", password)

    except ValueError:
        print("❌ Please enter a valid number.")

# Main Loop
while True:
    generate_password()

    again = input("\nDo you want to generate another password? (yes/no): ").lower()
    if again != "yes":
        print("\nThank you for using Password Generator 😊")
        break
