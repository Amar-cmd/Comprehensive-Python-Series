# ! List Comprehension

# * Traditional Method

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# new = []
#
# for x in fruits:
#     if "a" in x:
#         new.append(x)
#
# print(new)


# * List Comprehension

# new_list = [x for x in fruits if "a" in x]
# print(new_list)


# TODO: Eg 1 - Create a list of numbers from 0 to 9

# numbers = [x for x in range(10)]
# print(numbers)


# TODO: Eg 2 - Filtering elements (Only include numbers less than 5)

# numbers = [x for x in range(10) if x < 5]
# print(numbers)


# TODO: Eg 3 - Convert lowercase letters to uppercase

# text = "hello python"
# new_list = [item.upper() for item in text if item.isalpha()]
# print(new_list)


# TODO: Eg 4 - Extract even numbers from 1 to 20

# numbers = [num for num in range(1, 21) if num % 2 == 0]
# print(numbers)


# TODO: Eg 5 - Exclude a specific item ("apple")

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# item = [x for x in fruits if x != "apple"]
# print(item)


# TODO: Eg 6 - Replace "banana" with "orange"

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# new = [x if x != "banana" else "orange" for x in fruits]
# print(new)


# TODO: Eg 7 - Generate all possible pairs from two lists

# list1 = [1, 2, 3]
# list2 = ['A', 'B', 'C']
#
# pairs = [(x, y) for x in list1 for y in list2]
# print(pairs)


# TODO: Eg 8 - Convert all fruit names to uppercase

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# upper = [x.upper() for x in fruits]
# print(upper)


# TODO: Eg 9 - Set all values to "hello"

# item = ["a", 2, "cherry"]
#
# new = ["hello" for _ in item]
# print(new)


# TODO: Eg 10 - Flatten a nested list (convert a 2D list into a 1D list)
#
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# # ? syntax: [element for sublist in nested_list for element in sublist]
#
# print(matrix)
# new = [element for sublist in matrix for element in sublist]
# print(new)












