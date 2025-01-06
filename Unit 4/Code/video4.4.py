# ! Match-Case Code

# number = 7
#
# match number:
#     case 1: print("One")
#     case 2: print("Two")
#     case _: print("No Match")


# ! Match-Case -> Literal Matching

# code = 5000
#
# match code:
#     case 200: print("OK")
#     case 404: print("Not Found")
#     case 500: print("Internal Server Error")
#     case _: print("Unknown Status")


# ! Match-Case -> Variable Matching

# command = ("mul" , 3, 4)
#
# match command:
#     case ("add", x, y):
#         result = x + y
#     case ("sub", x, y):
#         result = x-y
#     case _:
#         result = "Invalid"
#
# print(result)


# ! Match-Case -> Sequence Matching

# data = [1, 2, 3, 4, 4, 5]
#
# match data:
#     case [x, y]:
#         print(x, y)
#     case [x, y, z]:
#         print(x, y, z)
#     case _:
#         print("Unknown")
