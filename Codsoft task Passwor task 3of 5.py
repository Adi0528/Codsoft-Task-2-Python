import secrets
import string

def generate_password(length, complexity):
    if complexity == "Low":
        characters = string.ascii_letters + string.digits
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "High":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
    else:
        return "Invalid complexity level"

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


while True:
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid positive integer for password length.")

complexity = input("Enter complexity level (Low, Medium, High): ")

generated_password = generate_password(length, complexity)
print(f"Generated Password: {generated_password}")