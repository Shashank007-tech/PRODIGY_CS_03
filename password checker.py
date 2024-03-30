import string

def password_strength(password):
   
    # Criteria for password strength
    length_ok = len(password) >= 8
    upper_ok = any(char.isupper() for char in password)
    lower_ok = any(char.islower() for char in password)
    digit_ok = any(char.isdigit() for char in password)
    special_ok = any(char in string.punctuation for char in password)

    # Determine password strength based on criteria
    if length_ok and upper_ok and lower_ok and digit_ok and special_ok:
        return "Strong password. Good job!"
    elif length_ok and (upper_ok or lower_ok) and digit_ok:
        return "Moderate password. Consider adding special characters."
    elif length_ok and (upper_ok or lower_ok):
        return "Weak password. Consider adding numbers and special characters."
    elif length_ok:
        return "Very weak password. Add uppercase letters, lowercase letters, numbers, and special characters."
    else:
        return "Password is too short. Password must be at least 8 characters long."

# Example usage:
password = input("Enter your password: ")
strength = password_strength(password)
print("Password strength:", strength)




