#? Looping Over Set

#* 1. Using for() loop

# my_set = {1, 2, 3, 4, 5}
# my_set = {"1", "2", "3", "4", "5"}

# for item in my_set:
#     print(item)



#* 2. Using while() loop

# my_set = {10, 20, 30, 40, 50}
# set_list = list(my_set)
#
# i = 0
# while i < len(set_list):
#     print(set_list[i])
#     i += 1


#* Looping Nested Set

# nested_set = {(1, 2), (3, 4), (5, 6)}
#
# for tup in nested_set:
#     print("Tuple: ", tup)
#     for value in tup:
#         print("\tValues: ", value)


#? Set Comprehension

#todo: Creating a set from a list

# numbers = [1, 2, 3, 4, 5]
# var = {number for number in numbers}
# print(var)


#todo: Keeping Only Even Numbers

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# var = {number for number in numbers if number % 2 == 0}
# print(var)


#todo: Extracting Unique Letters from a Word

# word = "banana"
# var = {letter for letter in word}
# print(var)


#todo:  Convert Words to Uppercase

# words = {"apple", "banana", "cherry"}
# var = {word.upper() for word in words}
# print(var)













