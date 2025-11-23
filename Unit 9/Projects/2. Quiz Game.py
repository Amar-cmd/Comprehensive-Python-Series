#! +-----------+
#! | QUIZ GAME |
#! +-----------+

quiz = {
    "What is the capital of India?": "Delhi",
    "Which planet is known as the Red Planet?": "Mars",
    "What is the largest mammal?": "Blue Whale",
    "How many days are there in a leap year?": "366",
    "Who wrote the Ramayana?": "Valmiki"
}

def display_menu():
    print("\n==== Quiz Game Menu ====")
    print("1. Start Quiz")
    print("2. View All Questions and Answers")
    print("3. Add a New Question")
    print("4. Delete a Question")
    print("5. Exit")
    print("=" * 24)


def start_quiz():

    score = 0

    print("\n--- Starting Quiz ---")

    for question, answer in quiz.items():
        print("\nQuestion")
        print(question)

        user_answer = input("Enter Your Answer: ").strip()

        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong! Correct Answer: ", answer)

    print("\n--- Quiz Complete ---")
    print(f"Your Score: {score} out of {len(quiz)}")
    print("-"*22)


def view_quiz():
    print("\n--- Quiz Questions & Answers ---")

    for q, a in quiz.items():
        print("Q: ", q)
        print("A: ", a)
    print("-"*35)


def add_question():
    question = input("Enter the new question: ").strip()
    answer = input("Enter the new answer: ").strip()

    if question in quiz:
        print("Question Already Exists!")
    else:
        quiz[question] = answer
        print("Question Added Successfully!")


def delete_question():
    question = input("Enter the new question: ").strip()

    if question in quiz:
        del quiz[question]
        print("Question Deleted Successfully")
    else:
        print("Question Not Found!")


while True:
    display_menu()

    choice = input("Enter Your Choice (1-5): ").strip()

    match choice:
        case "1":
            start_quiz()
        case "2":
            view_quiz()
        case "3":
            add_question()
        case "4":
            delete_question()
        case "5":
            print("Exiting")
            break
        case _:
            print("Invalid Choice. Please Try Again!")