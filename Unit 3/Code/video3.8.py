# ! Basic Assignment

# x = 10
# name = "Alice"
# print(x , name)


# ! Chained Assignment
# a = 10
# b = 10
# a = b = 10
# w = x = y= z = 20
#
# #? w = 20
# #? x = 20
# #? y = 20
# #? z = 20
#
# c = d = 10
# print(c, d)
#
#
# print(a, b)
# print(w,x,y,z)


# ! Multiple Assignment
# a, b, c = 1, 2, 3
# print(a, b ,c)
#
# a = 1
# b = 2
# c = 3
# print(a,b,c)


# a = 10
# b = 20
#
# Using Temporary Variable
# print(a, b)
# c = a
# a = b
# b = c
# print(a, b)


# Using Multiple Assignment
# Without Temporary Variable

# a, b = b, a
# print(a, b)


# ! Unpacking
# numbers = [1, 2 ,3]
# numbers = (4, 5 ,6, 7, 8)
# # a, b, *c = numbers
# *a ,b, c = numbers
# print(a)
# print(b)
# print(c)


# ! Augmented Assignment
# x = 10
# x = x + 5
# x += 5
# x -= 5
# x *= 5
# x /= 5
# x //= 5
# print(x)


# ! ================ KNOWLEDGE REINFORCEMENT ================

# TODO: Solution - 1
age = 25
course = "Python Programming"
print(age, course)

# TODO: Solution - 2
a = b = c = 50
print(a)
print(b)
print(c)

# TODO: Solution - 3
x, y, z = 5, 10, 15
print(x + y + z)


# TODO: Solution - 4
m = 100
n = 200
print(m, n)

m, n = n, m
print(m, n)


# TODO: Solution - 5
total = 0
total += 50  # 50
total -= 20  # 30
total *= 3  # 30*3 = 90
total /= 2  # 90/2 = 45.0
print("Total = ", total)
