# ! +---------+
# ! | Hangman |
# ! +---------+
import random


def show_menu():
    print("\n=== Hangman Game ===")
    print("1. Play Game")
    print("2. Exit")


def play_game():
    words = ["python", "hangman", "developer", "coding", "challenge"]
    word = random.choice(words)
    guessed_letters = []
    word_display = ["_"] * len(word)
    attempts = 6

    print(f"\nGuess the word. You have {attempts} attempts.")

    while attempts > 0 and "_" in word_display:
        print("\nWord: " + " ".join(word_display))
        print(f"Wrong attempts left: {attempts}")

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single character.")
            continue

        if guess in guessed_letters:
            print("You have already guessed this letter.")
            continue

        guessed_letters.append(guess)


        if guess in word:
            print("Good Guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    word_display[i] = guess
        else:
            print("Wrong Guess!")
            attempts -= 1

    if "_" not in word_display:
        print("\nCongrats! You guessed the word: ", word)
    else:
        print("\nGame Over! The word was:", word)


while True:
    show_menu()
    choice = input("Enter Your Choice: ").strip()

    match choice:
        case "1": play_game()
        case "2":
            print("Exiting Hangman")
            break
        case _:
            print("Invalid choice. Please select from the menu.")