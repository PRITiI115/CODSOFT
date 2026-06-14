import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("\n--- Password Generator ---")
try:
    length = int(input("Enter desired password length: "))
    if length < 8:
        print("Password length should be at least 8. Setting to 8.")
        length = 8

    password = generate_password(length)
    print("\nGenerated Password:", password)

except ValueError:
    print("Please enter a valid number!")
