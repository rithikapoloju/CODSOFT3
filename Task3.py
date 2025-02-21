import random
import string

def passwordgenerator(length=20, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    

    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Please select at least one character type."

    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Length must be a positive integer.")
        else:
            use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
            use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
            use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
            use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

            password = passwordgenerator(length, use_uppercase, use_lowercase, use_digits, use_symbols)
            print("Generated Password:", password)

    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")
