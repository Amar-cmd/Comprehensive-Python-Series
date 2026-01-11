
#! Using Regular Function
# def square(x):
#     return x ** 2
#
# print(square(5))


#! Using lambda Function
## lambda argument: expression

# square = lambda x: x ** 2
#
# print(square(6))


#* Example - 1
#? No Arguments

# say_hello = lambda: "Hello"
# print(say_hello())



#* Example - 2
#? Basic Usage

# x = lambda a: a + 10
# print(x(5))



#* Example - 3
#? Lambda with multiple arguments

# add = lambda a, b: a + b
# print(add(5, 3))




#* Example - 4
#? Lambda with Conditional Expression

# max_num = lambda a, b: a if a > b else b
# print(max_num(40, 7))



#* Example - 5
#? Lambda Inside Functions

# def make_multiplier(n):
#     return lambda x: x * n

# double = make_multiplier(2)
# triple = make_multiplier(3)

# print(double(5))
# print(triple(5))


#* Example - 6
#? Lambda in Dictionary

# operations = {
#     'add': lambda x, y: x + y,
#     'sub': lambda x, y: x - y
# }
# print(operations["add"](5, 3))
# print(operations["sub"](5, 3))


#* Example - 77
#? Lambda with sorted(key = ?)

# points = [(2, 3), (1, 2), (5, 1)]
# sorted_points = sorted(points, key= lambda x: x[1])
# print(sorted_points)