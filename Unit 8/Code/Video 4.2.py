#? Sets Basics

#* 1. Creating Sets

#  1.1 Using {}

# my_set = {1, 2, 3, 4, 4, 3, 2, 1}
# print(my_set)
# print(type(my_set))


# 1.2 Using set()

# my_list = set("Hello")
# print(my_list)
# print(type(my_list))


# 1.3 Creating Empty Set

# empty = set()
# print(empty)
# print(type(empty))


#! NOTE: VERY IMPORTANT

# my_set = {["a", 2]}
# print(my_set)


#* 2. Adding Elements to a set

# 2.1 Using .add() method

# my_set = {1, 2, 3}
# my_set.add(3)
# print(my_set)


# 2.2 Using .update() method

# my_set = {1, 2, 3, 4}
# my_set.update([5, 6, 7])
# print(my_set)

# my_set.update((8, 9))
# print(my_set)

# my_set.update("abc")
# print(my_set)



#* 3. Adding Elements to a set

# Using .remove() method
# my_set = {1, 2, 3, 4, 5}
# my_set.remove(3)
# print(my_set)
# my_set.remove(10)
# print(my_set)


# Using .discard() method

# my_set = {1, 2, 3, 4, 5}
# my_set.discard(3)
# print(my_set)
# my_set.discard(10)
# print(my_set)


# # Using .pop() method

# my_set = {10, 20, 30, 40, 50}
# my_set = {1, 2, 3, 4, 5}
# my_set.pop()
# print(my_set)

# # Popping from empty set
# empty = set()
# empty.pop()
# print(empty)


# Using .clear() method

# my_set = {1, 2, 3, 4, 5}
# my_set.clear()
# print(my_set)


# Using del keyword

# my_set = {1, 2, 3}
# del my_set
# print(my_set)









