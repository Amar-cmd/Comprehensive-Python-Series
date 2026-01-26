#! Basic I/O & Interaction
#* 1. print()
# print("Hello", "World", sep="-")

#* 2. input()
# name = input("Enter your name: ")
# print(name)


#! Sequence & Collection Helpers
#* 1. len()
# len([1, 2, 3, 4])

#* 2. range()
# for i in range(1, 5, 2):
#     print(i)

#* 3. list(), tuple(), set(), dict()
# print(list("abc"))
# print(tuple("abc"))
# print(set("abc"))
# print(dict(a=1, b=2))

#* 4. enumerate()
# for index, value in enumerate(['a', 'b', 'c']):
#     print(index, value)

#* 5. zip()
# print(list(zip([1, 2], ['a', 'b'])))

#* 6. sorted()
# print(sorted([3, 1, 2]))

#* 7. reversed()
# print(list(reversed([1, 2, 3])))


#! Functional-Style Tools

#* 1. map()
# print(list(map(str.upper, ['a', 'b', 'c'])))
# print(list(map(lambda x: x ** 2, [1,2,3,4])))

#* 2. filter()
# print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))

#* 3. any()
# print(any([0, False, 5]))
# print(any(x > 0 for x in [-1, -2, 3]))


#* 4. all()
# print(all([0, False, 5]))
# print(all(x > 0 for x in [1, 2, 3]))


#! Numeric & Math Utilities
#* 1. sum()
# print(sum([1, 2, 3, 4]))

#* 2. min(), max()
# print(min([3, 1, 4]))
# print(max([3, 1, 4]))
# print(min(["hi", "hello", "python"]))
# print(max(["hi", "hello", "python"]))

#* 3. abs()
# print(abs(-7))

#* 4. round()
# print(round(3.14159, 2))

#* 5. pow()
# print(pow(2, 3))

#* 6. divmod()
# print(divmod(17, 5))


#! Type Conversion & Checking
#* 1. int(), float(), str(), bool()
# print(int("5"))
# print(bool(0))

#* 2. type()
# print(type("hello"))

#* 3. isinstance()
# print(isinstance(5, int))


#! File & Dynamic Execution
#* 1. open()
# f = open('file.txt', 'r')
# print(f)

#* 2. eval()
# print(eval("2 + 3"))

#* 3. exec()
# code = """
# a = 5
# print(a)
# """
# exec(code)
