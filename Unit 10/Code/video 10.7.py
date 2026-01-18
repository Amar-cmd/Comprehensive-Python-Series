#! Recursion

#* Factorial Function
# 5! = 5x4x3x2x1 = 120
# Base Case: 0! = 1
# Recursive Case: n * (n - 1)

# def factorial(n: int):
#     if n == 0:
#         return 1 # base case
#     else:
#         return n * factorial(n-1) # recursive case
#
# print(factorial(5))


#* Fibonacci Sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21...

# Base Case: fib(0) = 0, fib(1) = 1
# Recursive Case: fib(n) = fib(n-1) + fib(n-2)

def fib(n: int):
    if n == 0: return 0
    elif n == 1: return 1

    else:
        return fib(n-1) + fib(n-2)

print(fib(7))








