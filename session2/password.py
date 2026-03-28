import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars):     
    """
    Generate a random password.

    Args:
    length (int): The length of the password.
    use_uppercase (bool): Whether to include uppercase letters.
    use_numbers (bool): Whether to include numbers.
    use_special_chars (bool): Whether to include special characters.

    Returns:
    str: The generated password.
    """
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    # Ensure password has at least one of each required character type
    password = ensure_password_quality(password, use_uppercase, use_numbers, use_special_chars)

    return password


def ensure_password_quality(password, use_uppercase, use_numbers, use_special_chars):
    """
    Ensure the password has at least one of each required character type.

    Args:
    password (str): The generated password.
    use_uppercase (bool): Whether to include uppercase letters.
    use_numbers (bool): Whether to include numbers.
    use_special_chars (bool): Whether to include special characters.

    Returns:
    str: The password with at least one of each required character type.
    """
    if use_uppercase and not any(char.isupper() for char in password):
        password = password + random.choice(string.ascii_uppercase)
    if use_numbers and not any(char.isdigit() for char in password):
        password = password + random.choice(string.digits)
    if use_special_chars and not any(char in string.punctuation for char in password):
        password = password + random.choice(string.punctuation)

    return password


def main():
    print("Password Generator")
    print("------------------")
    length = int(input("Enter the password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'    
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    print(f"Generated Password: {password}")


if __name__ == "__main__":
    main()