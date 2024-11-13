# ! Printing in python

# ? 1. Basic Usage of 'print()'

# print(34)
# print("Text")


# ? 2. Printing Multiple Items

# TODO: Print the following:
# TODO: x is 10 and y is 20

# x = 10
# y = 20
# print("x is", x, "and y is", y)


# TODO: Print equal sign (=) 100 times
# print("==========")
# print("=" * 100)

# print("THIS IS WHERE YOU CAN USE THIS:")
# # Using '-' for separation
# print('-' * 50)  # Prints '-' 50 times
# print("Section 1: Introduction")
# print('-' * 50)
#
# print("\nSome content here...\n")
#
# # Using '=' for separation
# print('=' * 50)  # Prints '=' 50 times
# print("Section 2: Details")
# print('=' * 50)
#
# print("\nMore content here...\n")
#
# # Another example with shorter lines
# print('-' * 20)
# print("End of Content")
# print('-' * 20)


# ? 3. Separator (sep=) parameter

# print("apple", "banana", "cherry", sep=" ")


# ? 4. End (end=) parameter

# print("This is output", end="...")
# print(1,2,3)
# print(1,2,3)
#
# print(1,2 ,3, end="...")
# print(1,2 ,3, sep="...")


# ? 5. Using Escape Characters

# TODO: print "hello world" in different line
# print("Hello")
# print("World")

# print("Hello\nWorld")
# print("Hello\tWorld")
# print("Hello\\World")


# ? 6. Format Strings:
# ? 6.1. Using "%" Sign

# name = "Gaurav"
# age = 22
# print("Name: %s and Age: %d" %(name, age))

# ? 6.2. Using "str.format()" method
# print("Name is {} and age is {}".format(name, age))
# print("Name is {} and age is {}".format(age, name))

# ? 6.3. Using "f-string"
# print(f"Name: {name} and Age: {age}")



# ? 7. Printing Data in Tabular Form
# headers = ["Name", "Age", "State"]
# data = [["Anvesha", 30, "Mumbai"],
#         ["Nitin", 25, "Punjab"],
#         ["Amar", 22, "Kerala"]]
#
# # Print headers and rows with a fixed width
# print("{:<10} {:<10} {:<15}".format(*headers))
# print("-" * 35)
# for row in data:
#     print("{:<10} {:<10} {:<15}".format(*row))




















































































