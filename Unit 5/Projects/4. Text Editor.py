# +-------------+
# * Text Editor *
# +-------------+


def add_text(current_text):
    new_text = input("Enter text to add: ")
    if current_text:
        current_text += " " + new_text
    else:
        current_text = new_text
    print("\nText Added!")
    return current_text


def view_text(current_text):
    if current_text:
        print("\nCurrent Text:\n" + current_text)
    else:
        print("\nThe document is empty.")


def find_and_replace(current_text):
    if not current_text:
        print("\nThe document is empty. Add text first")
        return current_text

    old = input("Enter word to find: ").strip()
    new = input("Enter word to replace with: ").strip()

    if old.lower() not in current_text.lower():
        print("Word Not Found!")
        return current_text

    words = current_text.split()
    modified_word = ""

    for word in words:
        if word.lower() == old.lower():
            modified_word += new + " "
        else:
            modified_word += word + " "

    print("\nWord Replaced.")
    return modified_word.strip()


def convert_case(current_text):
    if not current_text:
        print("\nThe document is empty. Add text first")
        return current_text

    case_choice = input("Enter 'U' for UPPERCASE and 'l' for lowercase: ").strip().lower()

    if case_choice == 'u':
        print("\nText Converted to UPPERCASE")
        return current_text.upper()

    elif case_choice == 'l':
        print("\nText Converted to lowercase")
        return current_text.lower()

    else:
        print("\nInvalid Option")
        return current_text


def reverse_text(current_text):
    if not current_text:
        print("\nThe document is empty. Add text first")
        return current_text

    reversed_text = current_text[::-1]
    print("\nReversed Text")
    return reversed_text


def clear_text():
    print("\nAll Text Cleared.")
    return ""


text = ""

while True:
    print("\nTEXT EDITOR MENU")
    print("1. Write Text")
    print("2. View Text")
    print("3. Find and Replace")
    print("4. Convert Case")
    print("5. Reverse Text")
    print("6. Clear Text")
    print("7. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice.isdigit():
        choice = int(choice)
    else:
        print("\nInvalid Choice. Please select a valid option.")
        continue

    match choice:
        case 1:
            text = add_text(text)
        case 2:
            view_text(text)
        case 3:
            text = find_and_replace(text)
        case 4:
            text = convert_case(text)
        case 5:
            text = reverse_text(text)
        case 6:
            text = clear_text()
        case 7:
            print("\nExiting the text editor. Goodbye!")
            break
        case _:
            print("\nInvalid Choice. Please Select a valid option.")
