import math

#! Commonly Used Constants
print(math.pi)    # Value of pi
print(math.e)     # Euler's number
print(math.tau)   # 2 * pi
print(math.inf)   # Infinity
print(math.nan)   # Not a Number

#! Rounding Functions
# floor() returns the largest integer less than or equal to the value
print(math.floor(3.9))    # 3
print(math.floor(-3.1))   # -4

# ceil() returns the smallest integer greater than or equal to the value
print(math.ceil(3.1))     # 4
print(math.ceil(-3.9))    # -3

# trunc() removes the decimal part
print(math.trunc(3.9))    # 3
print(math.trunc(-3.9))   # -3

#! Square Root, Power and Accurate Sum
# sqrt() returns square root
print(math.sqrt(49))      # 7.0

# pow() returns power as a float
print(math.pow(2, 3))     # 8.0

# fsum() gives more accurate floating-point sum
print(math.fsum([0.1, 0.2, 0.3]))   # 0.6

#! Euclidean Distance using hypot()
# hypot() calculates Euclidean distance
print(math.hypot(3, 4))   # 5.0
print(math.hypot(1, 2))

#! Exponential and Logarithm Functions
# exp(x) returns e raised to the power x
print(math.exp(1))        # 2.718...

# log(x, base) calculates logarithm with given base
print(math.log(8, 2))     # 3.0

# Optimized log functions
print(math.log2(8))       # 3.0
print(math.log10(100))    # 2.0

#! Trigonometry Functions
# Python trigonometric functions work with radians
angle = math.radians(90)

print(math.sin(angle))    # 1.0 approximately
print(math.cos(angle))
print(math.tan(angle))

#! Degree and Radian Conversion
degree_value = 90

# Convert degree to radians
radian_value = math.radians(degree_value)
print(radian_value)

# Convert radians to degree
print(math.degrees(radian_value))

#! Inverse Trigonometric Functions
print(math.asin(1))       # Inverse sine
print(math.acos(1))       # Inverse cosine
print(math.atan(1))       # Inverse tangent

#! Factorial, GCD and LCM
# factorial() calculates n!
print(math.factorial(5))  # 120

# gcd() returns greatest common divisor
print(math.gcd(12, 18))   # 6

# lcm() returns least common multiple
print(math.lcm(12, 18))   # 36

#! Combinations and Permutations
# comb(n, k) returns number of ways to choose k items from n items
print(math.comb(5, 2))    # 10

# perm(n, k) returns number of possible arrangements
print(math.perm(5, 2))    # 20

#! Floating-Point Comparison Problem
# Direct comparison of floating-point numbers can fail
print(0.1 + 0.2 == 0.3)   # False
# isclose() checks equality using tolerance
print(math.isclose(0.1 + 0.2, 0.3))   # True

#! Checking NaN and Infinity
value1 = math.nan
value2 = math.inf
value3 = 10

# Check whether value is NaN
print(math.isnan(value1))      # True

# Check whether value is infinity
print(math.isinf(value2))      # True

# Check whether value is a valid finite number
print(math.isfinite(value3))   # True
print(math.isfinite(math.inf)) # False
