# +-------------------+
# ? Encryption System *
# +-------------------+

import random
import string

print("\nMENU:")
print("1. Caesar Cipher Encryption")
print("2. Vowel Substitution Cipher")
print("3. Atbash Cipher")
print("4. ROT13 Cipher")
print("5. Combine Everything!!!")
print()

choice = int(input("Enter your encryption choice: "))
text = input("Enter the sentence for encryption:")


def caesar_cipher_encryption(sentence, shift):

    cipher = ""

    for char in sentence:
        if char.isupper():
            cipher += chr(((ord(char) - ord("A") + shift) % 26) + ord("A"))
        elif char.islower():
            cipher += chr(((ord(char) - ord("a") + shift) % 26) + ord("a"))
        else:
            cipher += char

    return cipher


def vowel_substitution_cipher(sentence):
    vowels = "aeiouAEIOU"
    encoded_sentence = ""

    for char in sentence:
        if char in vowels:
            encoded_sentence += str(random.randint(0, 9))
        else:
            encoded_sentence += char

    return encoded_sentence


def atbash_cipher(sentence):
    alphabet_lower = string.ascii_lowercase
    reverse_lower = string.ascii_lowercase[::-1]
    alphabet_upper = string.ascii_uppercase
    reverse_upper = string.ascii_uppercase[::-1]

    atbash = ""

    for char in sentence:
        if char.islower():
            index = alphabet_lower.index(char)
            atbash += reverse_lower[index]
        elif char.isupper():
            index = alphabet_upper.index(char)
            atbash += reverse_upper[index]
        else:
            atbash += char

    return atbash


def rot13_cipher(sentence):
    rot13 = ""

    for char in sentence:
        if char.isupper():
            rot13 += chr(((ord(char) - ord("A") + 13) % 26) + ord("A"))
        elif char.islower():
            rot13 += chr(((ord(char) - ord("a") + 13) % 26) + ord("a"))
        else:
            rot13 += char

    return rot13


match choice:
    case 1:
        n = int(input("Specify shift: "))
        encryption = caesar_cipher_encryption(text, n)
        print(encryption)
    case 2:
        encryption = vowel_substitution_cipher(text)
        print(encryption)

    case 3:
        encryption = atbash_cipher(text)
        print(encryption)

    case 4:
        encryption = rot13_cipher(text)
        print(encryption)

    case 5:
        encryption = vowel_substitution_cipher(rot13_cipher(atbash_cipher(caesar_cipher_encryption(text, 5))))
        print(encryption)

    case _: print("Invalid Choice.")