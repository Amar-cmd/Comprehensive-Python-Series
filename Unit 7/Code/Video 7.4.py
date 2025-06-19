#? Looping Tuple

#* 1. For Loop
# fruits = ("apple", "banana", "cherry")

# for fruit in fruits:
#     print(fruit)

# for i in range(len(fruits)):
#     print(fruits[i])


#* 2. enumerate()
# fruits = ("apple", "banana", "cherry")
# for idx, item in enumerate(fruits):
#     print(idx, item)


#* 3. While Loop
# fruits = ("apple", "banana", "cherry")
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1



#* 4. Loop Backward
# fruits = ("apple", "banana", "cherry")

#! 4.1 Using reversed()

# for fruit in reversed(fruits):
#     print(fruit)

#! 4.2 Using Slicing
# for fruit in fruits[::-1]:
#     print(fruit)



#? Looping Tuple

#* 1. Concatenation (+)
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# tuple3 = tuple1 + tuple2
# print(tuple3)


#* 2. Repetition (*)

# tuple1 = ("A", "B", "C")
# tuple2 = tuple1 * 3
# print(tuple2)



#* 3. Using sum()

# tuple1 = (1, 2)
# tuple2 = (3, 4)
# tuple3 = (5, 6)
# result = sum((tuple1, tuple2, tuple3), ())
# print(result)