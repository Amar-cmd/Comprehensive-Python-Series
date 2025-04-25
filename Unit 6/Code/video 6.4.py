#! Looping in List

#* 1. Using For Loop
# fruits = ["apple", "banana", "cherry"]

#? 1.1 Normal For Loop
# for fruit in fruits:
#     print(fruit)

#? 1.2 For Loop Using Indexing
# for i in range(len(fruits)):
#     print(i, fruits[i])

#* 2. Using While Loop
# fruits = ["apple", "banana", "cherry"]

# i = 0
# while i<len(fruits):
#     print(fruits[i])
#     i += 1


#* 3. Looping through a nested list (2D List)

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# for rows in matrix:
#     for items in rows:
#         print(items)

#* 4. Using enumerate()

# fruits = ["apple", "banana", "cherry"]

# for idx, item in enumerate(fruits):
#     print(idx, item)


#* 5. Using zip()

# fruits = ["apple", "banana", "cherry"]
# index = [1, 2, 3]

# for idx, fruit in zip(index, fruits):
#     print(idx, fruit)


#* 6. Using reversed()

#? 6.1 Normal reverse
# fruits = ["apple", "banana", "cherry"]

# for item in reversed(fruits):
#     print(item)

#? 6.2 Using slicing
# for item in fruits[::-1]:
#     print(item)