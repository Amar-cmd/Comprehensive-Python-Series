# * ##################################
# ! for Loop Example Code
# * ##################################

# fruits = ["apple", "banana", "cherry"]
#
# for fruit in fruits:
#     print(fruit)

# * ##################################
# ! Loop Control Example - Break
# * ##################################

# fruits = ["apple", "banana", "cherry"]
#
# for fruit in fruits:
#     if fruit == "banana":
#         break
#     print(fruit)

# * ##################################
# ! Loop Control Example - continue
# * ##################################

# fruits = ["apple", "banana", "cherry"]
#
# for fruit in fruits:
#     if fruit == "banana":
#         continue
#     print(fruit)

# * ##################################
# ! Loop Control Example - pass
# * ##################################

# fruits = ["apple", "banana", "cherry"]
#
# for fruit in fruits:
#     # complicated loop
#     ...
#
# print(123)

# * ##################################
# ! for-else loop Example
# * ##################################

# nums = [1,2,3]
# target = 2
#
# for item in nums:
#     if item == target:
#         print("Target is found")
#         break
# else:
#     print("Target is not found")

# * ##################################
# ! for-else Loop Control Example - break
# * ##################################

# fruits = ["apple", "banana", "cherry"]
#
# for fruit in fruits:
#     if fruit == "banana":
#         break
#     print(fruit)
# else:
#     print("NO more fruits left!")

# * ##################################
# ! for-else Loop Control Example - continue
# * ##################################

# fruits = ["apple", "banana", "cherry"]
#
# for fruit in fruits:
#     if fruit == "banana":
#         continue
#     print(fruit)
# else:
#     print("NO more fruits left!")

# * ##################################
# ! Nested For Loop (Example)
# * ##################################

# outer_list = [1, 2]
# inner_list = ["a", "b", "c"]
#
# for outer_item in outer_list:
#     for inner_item in inner_list:
#         # Code Block
#         print(outer_item, inner_item)

# * ##################################
# ! For loop with string
# * ##################################

# s = "hello"
# for char in s:
#     print(char)

# * ##################################
# ! For loop with list
# * ##################################

# l = [1,2,3]
#
# for i in l:
#     print(i)

# * ##################################
# ! For loop with tuple
# * ##################################

# l = (4,5,6)
#
# for i in l:
#     print(i)

# * ##################################
# ! For loop with dictionary
# * ##################################

dict = {"a": 1, "b": 2}

# ? keys
# for key in dict:
#     print(key)

# ? values
# for value in dict.values():
#     print(value)

# ? key-value
# for key, value in dict.items():
#     print(key, value)

# * ##################################
# ! For loop with range()
# * ##################################

# for i in range(5): #stop param
#     print(i)

# for i in range(1, 5): # start, stop param
#     print(i)

# for i in range(1, 11, 2): # start, stop, step param
#     print(i)


# for i in range(5, 1, -1):
#     print(i)

# for i in range(1, 5, -1):
#     print(i)

# * ##################################
# ! For loop with enumerate()
# * ##################################

# fruits = [ "apple", "banana", "cherry"]
# counter = 0
#
# for item in fruits:
#     print(item, counter)
#     counter += 1


# for idx, item in enumerate(fruits):
#     print(idx, item)

# * ##################################
# ! For loop with zip()
# * ##################################

# names = ["Amar", "Anvesha", "Nitin"]
# ages = [24, 28, 30]
#
# # result = zip(names, ages)
# # print(list(result))
#
#
# for name, age in zip(names, ages):
#     print(name, age)

# * ##################################
# ! For loop with _
# * ##################################

# for _ in range(3):
#     print("Hello")
