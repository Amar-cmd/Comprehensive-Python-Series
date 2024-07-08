# ! Operators in Python

# ? ARITHMETIC OPERATORS

a = 10
b = 20

# * 1. Addition (+)
add = a + b
# print(f"Addition: {a} + {b} = {add}")

# * 2. Subtraction (-)
sub = a - b
# print(f"Subtraction: {a} - {b} = {sub}")

# * 3. Multiplication (*)
mul = a * b
# print(f"Multiplication: {a} * {b} = {mul}")

# * 4. Division (/)
div = a / b
# print(f"Division: {a} / {b} = {div}")

# * 5. Modulus (%)
mod = a % b
# print(f"Modulus: {a} % {b} = {mod}")

# * 6. Exponentiation (**)
exp = a ** b
# print(f"Exponentiation: {a} ** {b} = {exp}")

# * 7. Floor Division (//)
floordiv = a // b
# print(f"Floor Division: {a} // {b} = {floordiv}")




# ? ASSIGNMENT OPERATORS

# * 1. Assign (=)
a = 10
# print(f"Assign: a = 5 -> {a}")

# * 2. Add and Assign (+=)
a += 10     # a = a + 10
# print(f"Add and Assign: a += 10 -> {a}")

# * 3. Subtract and Assign (-=)
a -= 1
# print(f"Subtract and Assign: a -= 1 -> {a}")

# * 4. Multiply and Assign (*=)
a *= 3
# print(f"Multiply and Assign: a *= 3 -> {a}")


# * 5. Divide and Assign (/=)
a /= 2
# print(f"Divide and Assign: a /= 2 -> {a}")


# * 6. Modulus and Assign (%=)
a %= 3
# print(f"Modulus and Assign: a %= 3 -> {a}")


# * 7. Exponent and Assign (**=)
a **= 2
# print(f"Exponent and Assign: a **= 2 -> {a}")


# * 8. Floor division and Assign (//=)
a //= 2
# print(f"Floor Division and Assign: a //= 2 -> {a}")

# * 9. Bitwise AND and Assign (&=)
# * 10. Bitwise OR and Assign (|=)
# * 11. Bitwise XOR and Assign (^=)
# * 12. Bitwise Right Shift and Assign (>>=)
# * 13. Bitwise Left Shift and Assign (<<=)



# ? COMPARISON OPERATORS

# a = 10
# b = 20

# * 1. Equal (==)
eq = a == b
# print(f"Equal: {a} == {b} is {eq}")

# * 2. Not Equal (!=)
neq = a != b
# print(f"Not Equal: {a} != {b} is {neq}")

# * 3. Greater than (>)
gt = a > b
# print(f"Greater Than: {a} > {b} is {gt}")

# * 4. Less than (<)
lt = a < b
# print(f"Less Than: {a} < {b} is {lt}")


# * 5. Greater than or equal to (>=)
gte = a >= b
# print(f"Greater Than or Equal To: {a} >= {b} is {gte}")

# * 6. Less than or equal to (<=)
lte = a <= b
# print(f"Less Than or Equal To: {a} <= {b} is {lte}")




# ? LOGICAL OPERATORS

a = True
b = False

# * 1. AND (and)
and_op = a and b
# print(f"Logical AND: {a} and {b} = {and_op}")


# * 2. OR (or)
or_op = a or b
# print(f"Logical OR: {a} or {b} = {or_op}")


# * 3. NOT (not)
not_op = not a
# print(f"Logical NOT: not {a} = {not_op}")




# ? BITWISE OPERATORS

# a = 10 # In binary: 1010
# b = 4 # In binary: 0100

# * 1. Bitwise AND (&)
bit_and_op = a & b
# print(f"Bitwise AND: {a} & {b} = {bit_and_op} (binary: {a:04b} & {b:04b} = {bit_and_op:04b})")

# * 2. Bitwise OR (|)
bit_or_op = a | b
# print(f"Bitwise OR: {a} | {b} = {bit_or_op} (binary: {a:04b} | {b:04b} = {bit_or_op:04b})")

# * 3. Bitwise XOR (^)
bit_xor_op = a ^ b
# print(f"Bitwise XOR: {a} ^ {b} = {bit_xor_op} (binary: {a:04b} ^ {b:04b} = {bit_xor_op:04b})")

# * 4. Bitwise NOT (~)
bit_not_op = ~a
# print(f"Bitwise NOT: ~{a} = {bit_not_op} (binary: ~{a:04b} = {bit_not_op:04b})")

# * 5. Bitwise Left Shift (<<)
left_shift = a << 2
# print(f"Bitwise Left Shift: {a} << 2 = {left_shift} (binary: {a:04b} << 2 = {left_shift:08b})")

# * 6. Bitwise Right Shift (>>)
right_shift = a >> 2
# print(f"Bitwise Right Shift: {a} >> 2 = {right_shift} (binary: {a:04b} >> 2 = {right_shift:04b})")



# ? IDENTITY OPERATORS

a = [1,2,3,4,5]
b = [1,2,3,4,5]
c = a

# * 1. IS (is)
is_op = a is b
# print(f"{a} is {b} = {is_op}")

is_op = a is c
# print(f"{a} is {c} = {is_op}")
# print(id(a))
# print(id(b))
# print(id(c))

# * 2. IS NOT (is not)
is_not_op = a is not c
# print(f"{a} is not {c} = {is_not_op}")

is_not_op = a is not b
# print(f"{a} is not {c} = {is_not_op}")









# ? MEMBERSHIP OPERATORS

my_list = [1,2,3,4,5]
my_string = "Python"

# * 1. IN (in)
in_list = 3 in my_list
# print(f"3 in {my_list} = {in_list}")

in_string = "Hello" in my_string
# print(f"'Hello' in '{my_string}' = {in_string}")


# * 2. NOT IN (not in)
not_in_list = 6 not in my_list
# print(f"6 not in {my_list} = {not_in_list}")

not_in_string = "Python" not in my_string
# print(f"'Python' not in '{my_string}' = {not_in_string}")




# ? WALRUS OPERATORS

# todo: Checked without walrus operator
a = [1,2,3,4,5]
n = len(a)
# if n > 3:
#     print("List is greater than 3. (Checked without Walrus Operator")



# todo: Checked with walrus operator
# if (n := len(a)) > 3:
#     print("List is greater than 3. (Checked with Walrus Operator")






















