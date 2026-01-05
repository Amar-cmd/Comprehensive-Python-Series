#! Functions - Part 2

#* Types of Arguments:
#? 1. Positional Arguments:

# def sub(a, b):
#     return a-b
# print(sub(5, 10))
# print(sub(10, 5))

#? 2. Keyword Argument:

# def introduce(name, age):
#     print(f"Hi, {name}. You are {age} years old")
#
# introduce(name="amar", age="18")
# introduce(age="18", name="amar" )


#? 3. Default Arguments

# def greet(name = "guest"):
#     print(f"Hello {name}")
#
# greet()
# greet("amar")

#! IMPORTANT POINT
# def greet(age = 18, name): # ❌ Incorret!: SyntaxError: parameter without a default follows parameter with a default
# def greet(name, age = 18): # ✔️ Correct!
#     print(f"Hello {name}. You are {age}.")
#
# greet("amar")


#? 4. Variable Length Arguments - *args

# # Meaning of * in *args
# items = (1, 2, 3, 4, 5)

# # Normal Assignment
# a, b, c, d, e = items
# print(a)

# # Using *
# a, *b = items
# print(a, b)

# def add_nums(*args):
#     print(sum(args))
#
# add_nums(1,2,3, 7, 10,22)


#? 5. Variable Length Arguments - **kwargs

# def info(**kwargs):
#     for key, value in kwargs.items():
#         print(key, " → ",value)
#
# info(name="Amar", age= 18, city = "Delhi")


#? Combining all types of arguments

#? Order:
#* normal params → *args → default params → **kwargs

# def demo(a, b, *args, city = "unknown", **kwargs):
#     print(a, b)
#     print(args)
#     print(city)
#     print(kwargs)
#
# demo(1,2,3,4,5, city="Delhi", country="India", pincode = 123456)