#* Most Common Errors

#? 1. Syntax Error
# if 5 % 2 == 0:
#     print("even")


# ? 2. Indentation Error
# if 5 % 2 == 0:
#     print("even")

# ? 3. Name Error
# n = 5
# if n % 2 ==0:
#     print("even")

#? 4. Type Error

## Int + str
# print(2 + 2)

## calling non callable function
# x = 5
# x()

## Passing wrong or extra argument
# len(1, 2)



#? 5. Value Error
# int("abc")
# range(1, 10, 0)

#? 6. Attribute Error
# [1,2].strip()
# [1,2].indexx()


#? 7. Index Error
# x = [1,2]
# print(len(x) - 1)
# print(x[1])


#? 8. Key Error
# fruit = {"name": "apple", "color": "red"}
# print(fruit.get("price"))


#? 9. Zero Division Error
# print(10/0)


#? 10. File Not Found Error
# open("file.txt")


#? 11. Import Error / Module Not Found Error

# from random import  abc
# import asld

#? 12. Assertion Error

# x= -5
# assert x > 0, "x must be non-negative"












