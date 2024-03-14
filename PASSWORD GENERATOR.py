import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    length = int(input("Enter the desired password length (default is 12): "))
except ValueError:
    print("Invalid input. Using default password length of 12.")
    length = 12

password = generate_password(length)
print(f"Generated Password: {password}")
