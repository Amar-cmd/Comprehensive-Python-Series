# class Car:
#     wheels = 4
#     total_cars = 0
#
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#         Car.total_cars += 1
#
#     def info(self):
#         print(f"{self.brand}, {self.color}")

# class Book:
#     total_books = 0
#
#     def __init__(self, title, author, lang="HI"):
#         self.title = title
#         self.author = author
#         self.lang = lang
#         Book.total_books += 1
#
#     @classmethod
#     def show_count(cls):
#         print(cls.total_books)
#
# b1 = Book("1984", "Orwell")
# Book.show_count()
#
# b2 = Book("Dune", "Herbert")
# Book.show_count()


# Using classmethod() function

# class Book:
#     total_books = 0
#
#     def show_count(cls):
#         print(cls.total_books)
#
#     show_count = classmethod(show_count)
#
# Book.show_count()


# Using @staticmethod decorator

# class MathTools:
#
#     @staticmethod
#     def add(a, b):
#         return a + b
#
# print(MathTools.add(2, 3))
#
# m = MathTools()
# print(m.add(4, 6))



# Using staticmethod() function

class MathTools:

    def add(a, b):
        return a + b

    add = staticmethod(add)

print(MathTools.add(2, 3))














