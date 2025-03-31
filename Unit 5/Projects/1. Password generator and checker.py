# +----------------------------+
# Password Generator & Checker |
# +----------------------------+
import random
import string

print("MENU:")
print("1. Generate Password")
print("2. Check Password Strength")
print()

choice = int(input("Enter Your Choice: "))


def make_password(length):
    letters = string.ascii_letters
    numbers = string.digits
    punctuations = string.punctuation
    all_characters = letters + numbers + punctuations

    new_password = ""
    for _ in range(length):
        new_password += random.choice(all_characters)
    return new_password


def check_password_strength(check_password):
    length_ok = False
    upper_ok = False
    lower_ok = False
    digits_ok = False
    special_ok = False

    if len(check_password) >= 8:
        length_ok = True

    for char in check_password:
        if char.isupper(): upper_ok = True
        if char.islower(): lower_ok = True
        if char.isdigit(): digits_ok = True
        if char in string.punctuation: special_ok = True

    score = 0
    if length_ok: score += 1
    if upper_ok: score += 1
    if lower_ok: score += 1
    if digits_ok: score += 1
    if special_ok: score += 1

    if score == 5:
        return "Strong Password"
    elif score >= 3:
        return "Moderate Password"
    else:
        return "Weak Password"


match choice:
    case 1:
        password_length = int(input("Enter length of the password: "))
        password = make_password(password_length)
        print("Your Password is: ", password)
    case 2:
        password = input("Enter Your Password: ")
        strength = check_password_strength(password)
        print(strength)
    case _:
        print("Invalid Choice")
