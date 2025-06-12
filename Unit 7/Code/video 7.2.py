#! TUPLES BASICS

#? Creating Tuples:

#* Using Basic Parenthesis()
# my_tuple = (1, 2, 3)

#* Single Element Tuple
# my_tuple = (1,)

#* using tuple constructor
# my_list = [1, 2, 3]

#* Empty Tuple
# my_tuple = ()

#* Nested Tuple
# nested_tuple = (1, (1, 2), 3)

#* Mixed Tuple
# mixed_tuple = ("a", 12, True, 3.14)
# print(type(mixed_tuple))


#? Creating Tuples:

#* 1. Indexing...
# my_tuple = (10, 20, 30)
# print(my_tuple[0])
# print(my_tuple[1])
# print(my_tuple[2])

#* 2. Negative Indexing...
# print(my_tuple[-1])
# print(my_tuple[-2])
# print(my_tuple[-3])

#* 3. Slicing...
# my_tuple = (10, 20, 30)
# print(my_tuple[0:2])


#* Accessing Nested Tuple
# nested_tuple = ((1, 2), (3, 4))

# print(nested_tuple[0])
# print(nested_tuple[0][0])
# print(nested_tuple[0][1])
# print(nested_tuple[1])
# print(nested_tuple[1][0])
# print(nested_tuple[1][1])


#? Updating Tuples:

#* 1. Convert to list and modify

# my_tuple = (1, 2, 3)
# #TODO: Replace 2 with 20.

# # my_tuple[1] = 20 # ❌❌

# my_list = list(my_tuple)  # Convert to list
# my_list[1] = 20           # Modify element
# my_tuple = tuple(my_list) # Convert back to tuple
# print(my_tuple)

#* 2. Concatenation (+)
# my_tuple = (1, 2, 3)
# new_tuple = my_tuple + (4, 5)
# print(new_tuple)
# print(my_tuple)


#? Unpacking Tuples:

#* 1. Known number of values
# my_tuple = (1, 2, 3)
# a, b, c = my_tuple
# print(a)
# print(b)
# print(c)


#* 2. Unknown number of values
#* Extended Unpacking (*)

# my_tuple = (1, 2, 3, 4, 5)

# a, *c ,b = my_tuple
# print(a)
# print(b)
# print(c)


#! ERRORS while handling tuple unpacking

# my_tuple = (1, 2, 3, 4, 5)

#* 1. Fewer variables • More elements

# a, b = my_tuple
# print(a)

#* 2. Fewer elements • More variables

# my_tuple = (1, 2)
# a, b, c = my_tuple


#* 3. Ignoring values

#* Using Underscore (_)

# my_tuple = (1, 2, 3)
# a, _ ,b = my_tuple
# print(a, b)