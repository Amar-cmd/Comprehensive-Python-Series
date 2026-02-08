#! Error Handling

#? try-except

# TODO: Calculate user's age in 5 years
# try:
#     age = int(input("Enter your age: "))
#     print(age + 5)
# except ValueError as e:
#     print("Error: Please enter a valid number")


# ? try-except...except

# TODO: Fetch Fruits using index number

# try:
#     item = ["apple", "mango"]
#     index = int(input("Enter index to fetch fruit: "))
#     print(item[index])
# except ValueError:
#     print("Error: Index must be a number")
#
# except IndexError:
#     print("Error: Choose index within the range")


# ? try-except...else

# TODO: Calculate total price

# try:
#     price = float(input("Enter item price: "))

#     quantity = int(input("Enter quantity: "))
#     total = price * quantity
#
# except ValueError:
#     print("Error: Please enter a valid number")
#
# else:
#     print(f"Total Cost: ₹{total}")


# ? try-finally

# TODO: divide by 0

# try:
#     result = 10 / 0
#     print(result)
#
# finally:
#     print("End of operation")


# ? try-except...finally

# TODO: divide by 0

# try:
#     result = 10 / 0
#     print(result)
#
# except ZeroDivisionError:
#     print("Error: You can't divide by 0")
#
# finally:
#     print("End of operation")