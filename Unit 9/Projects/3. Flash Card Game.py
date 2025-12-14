#! +-----------------+
#! | FLASH CARD GAME |
#! +-----------------+

flashcards = {
    "What is the keyword to define a function in Python?": "def",
    "Which data type is used to store True or False values?": "Boolean",
    "What symbol is used to comment a single line in Python?": "#",
    "What is the output of 3 ** 2 in Python?": "9",
    "Which Python data structure stores key-value pairs?": "Dictionary"
}

def display_menu():
    print("\n==== Flash Card Menu ====")
    print("1. Play Flashcards")
    print("2. View All Flashcards")
    print("3. Add a New Flashcard")
    print("4. Delete a Flashcard")
    print("5. Exit")
    print("="*25)


def play_flashcard():
    print("\n--- Flashcard Session Started ---")
    for question, answer in flashcards.items():
        print("\nQuestion: ")
        print(question)
        input("Press Enter to see the answer")
        print("Answer", answer)
    print("\n--- End of Session ---")


def view_flashcards():
    print("\n--- Flashcard List ---")
    for question, answer in flashcards.items():
        print("Q: ", question)
        print("A: ", answer)
    print("-"*22)


def add_flashcard():
    question = input("Enter the new question: ").strip()
    answer = input("Enter the new answer: ").strip()

    if question in flashcards:
        print("Flashcard Already Exists!")
    else:
        flashcards[question] = answer
        print("Flashcard Added Successfully!")


def delete_flashcard():
    question = input("Enter the new question you want to delete: ").strip()

    if question in flashcards:
        del flashcards[question]
        print("Flashcard Deleted Successfully")
    else:
        print("Flashcard Not Found!")



while True:
    display_menu()

    choice = input("Enter your choice (1-5): ").strip()

    if choice == '1':
        play_flashcard()
    elif choice == '2':
        view_flashcards()
    elif choice == '3':
        add_flashcard()
    elif choice == '4':
        delete_flashcard()
    elif choice == '5':
        print("Exiting!")
        break
    else:
        print("Invalid choice. Please try again!")