import random
import string

def generate_password(length, strength):
    characters = ""

    if strength == "weak":
        characters = string.ascii_letters + string.digits
    elif strength == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif strength == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
    else:
        raise ValueError("Invalid strength level. Choose 'weak', 'medium', or 'strong'.")

    if not characters:
        raise ValueError("Invalid strength level. Choose 'weak', 'medium', or 'strong'.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length, strength):
    passwords = [generate_password(length, strength) for _ in range(num_passwords)]
    return passwords

def main():
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        password_length = int(input("Enter the desired length of the password: "))
        strength = input("Choose password strength (weak/medium/strong): ").lower()

        passwords = generate_multiple_passwords(num_passwords, password_length, strength)
        print("\nGenerated passwords:")
        for i, password in enumerate(passwords, start=1):
            print(f"Password {i}: {password}")
    except ValueError:
        print("Invalid input. Please enter valid values.")

if __name__ == "__main__":
    main()
