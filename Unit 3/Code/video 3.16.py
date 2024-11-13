# if True:
#     print("This is fine")
# print("This is not fine")


# # This will work
# x = 10 # This will also work
# print(x)


# This is first line
# This is second line
# x = 10
# print(x)
#
#
# """
# This is multiple line comment too...
# """
# y = 10
# print(y)


# def add(a,b):
#     """
#     This function adds two numbers.
#
#     Parameters:
#     a (int, float): The first number.
#     b (int, float): The second number.
#
#     Returns:
#     int, float: The sum of the two numbers.
#     """
#     return a+b
#
# # print(add.__doc__)
# print(help(add))


# def fn():
#     x = 10
#     print(x)
#
# fn()
# print(x)


# def o_fn():
#
#     x = 10 # Enclosing Scope
#
#     def i_fn():
#
#         print(x) # Accessing variable "x" from outer function
#
#     i_fn()
# o_fn()


# x = 10
# def fn():
#     print(x)
#
# fn()
#
# print(x)


# def myfunc():
#     # create a global variable
#     global x
#     x = 10
#
#
# myfunc()
#
# print(x)


# x = 30
#
# def my_function():
#     global x
#     x = 40  # modifies the global variable x
#     print(x)  # prints 40
#
# my_function()
# print(x)  # prints 40




# def outer():
#     x = "outer"
#
#     def inner():
#         nonlocal x
#         x = "inner"
#         print(x)
#
#     inner()
#     print(x)
#
# outer()


# ? Summary

# x = "global"
#
# def outer_function():
#     x = "enclosing"
#
#     def inner_function():
#         x = "local"
#         print(x)
#
#     inner_function()
#
# outer_function()














