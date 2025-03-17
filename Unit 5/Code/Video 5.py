# ! 1. String Module

# * Import it first
# import string

# * ASCII Letters
# print(string.ascii_letters)

# * Lower Case Letters
# print(string.ascii_lowercase)

# * Upper Case Letters
# print(string.ascii_uppercase)

# * digits
# print(string.digits)


# * hexdigits
# print(string.hexdigits)


# * octdigits
# print(string.octdigits)


# * Punctuations
# print(string.punctuation)


# * Whitespaces
# print(string.whitespace)


# * Printables
# print(string.printable)

# ================================================================================================

# ! 2. String Functions

# * Template Class
# from string import Template

# template = Template("Course: $a\nPrice: $b")
# result = template.substitute(a = "Python Mastery Series", b = "FREE")

# print(result)


# * Formatter
# from string import Formatter

# formatter = Formatter()
# result = formatter.format("HI {}", "amar")

# print(result)


# * capwords
# import string

# txt = "      hEllo       ,  WORld"

# print(string.capwords(txt))
