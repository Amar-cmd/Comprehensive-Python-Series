# +------------------------+
# ? 4. Calculator
# +------------------------+

# Creating Menu
def display_menu():
    print("\nSimple Calculator Menu")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Modulus (%)")
    print("7. Square Root (√)")
    print("8. Quit")
    print("-" * 30)


while True:
    display_menu()
    choice = int(input("Choose an operation (1-8): "))
    num = num1 = num2 = None  # Placeholder values. will be assigned based on user's choice

    if choice in [1, 2, 3, 4, 5, 6]:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

    if choice == 7:
        num = float(input("Enter a number: "))

    match choice:
        case 1:
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        case 2:
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        case 3:
            print(f"Result: {num1} x {num2} = {num1 * num2}")
        case 4:
            if num2 == 0:
                print("ERROR: Division by 0 is not allowed.")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
        case 5:
            print(f"Result: {num1} ^ {num2} = {num1 ** num2}")
        case 6:
            if num2 == 0:
                print("ERROR: Modulus by zero is not allowed.")
            else:
                print(f"Result: {num1} % {num2} = {num1 % num2}")

        case 7:
            if num < 0:
                print("ERROR: Square root of a negative number is not defined.")
            else:
                print(f"Result: √{num} = {num ** 0.5}")
        case 8:
            print("Exiting the calculator. Goodbye!")
            break
        case _:
            print("Invalid Choice. Please select a valid operation")
