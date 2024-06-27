# ! Common Type Conversion Functions

# ? 1. int()

# a = 3.14
a = int(3.14)
# print(a, "->", type(a))

# ? 2. float()

b = float(3)
# print(b, "->", type(b))

# ? 3. str()

# c = 100
c = str(100)
# print(c, "->", type(c))

# ? 4. list()

# d = "hello"
d = list("hello")
# print(d, "->", type(d))

# ? 5. tuple()

e = tuple("hello")
# print(e, "->", type(e))

# ? 6. set()

f = set("hello")
# print(f, "->", type(f))

# ? 7. bool()
g1 = bool(2)
g2 = bool()
# print(g1, "->", type(g1))
# print(g2, "->", type(g2))


# ! Type casting as result of calculations

# * Implicit Type Casting

# ? 1. Addition of Integer and Float:

num_int = 10
num_float = 10.5
# print(num_int+num_float)
# print(type(num_int+num_float))


#  ? 2. Float to Complex:
num_complex = 2 + 5j
# print(num_float + num_complex, type(num_float+num_complex))



#  ? 3. Division of Integers Resulting in Float:

n1 = 10
n2 = 3
# print(n1/n2, type(n1/n2))


# * Explicit Type Casting
#  ? 1. Integer Division with Explicit Type Casting:

n3 = int(n1/n2)
# print(n3, type(n3))



#  ? 2. Sum of Numbers from a String Input:

str_n1 = int("4")
str_n2 = int("5")
# print(str_n1 + str_n2)


# ! Common Errors

#  ? 1. Invalid String Format for Numeric Conversion:

# print(int("123abc"))
# print(float("12.24.12"))


#  ? 2. Empty String Conversion:
# print(int(""))
# print(float(""))


#  ? 3. Incorrect Use of Type Casting Functions:
# print(int(123.45,10))

#  ? 4. Incorrect Data Types for Type Casting:
# print(int([1,2,3]))


#  ? 5. Naming Conflicts with Built-in Functions:

# int = 10
# print(int("123"))

#  ? 6. String Representing Complex Numbers:

# print(float("2+3j"))
# print(int("2+3j"))












