#! public
# class Book:
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price
#
# b = Book("Python Basics", 399)
# print(b.price)
# b.price = -10
# print(b.price)


#! protected
# class Car:
#     def __init__(self, model, max_speed):
#         self.model = model
#         self._max_speed = max_speed
#
#     def show_info(self):
#         print(f"{self.model} can go upto {self._max_speed} km/h")
#
# c = Car("Tesla", 250)
# c.show_info() # recommended
# print(c._max_speed) # technically allowed, but bad style



#! private

# class Car:
#     def __init__(self, model, max_speed):
#         self.model = model
#         self.__max_speed = max_speed
#
#     def show_info(self):
#         print(f"{self.model} can go upto {self.__max_speed} km/h")
#
# c = Car("Tesla", 250)
# c.show_info() # recommended
# # print(c.__max_speed) # AttributeError
#

#? Name Mangling
# # print(c._Car__max_speed) # HIGHLY DISCOURAGED!





from dataclasses import dataclass

@dataclass
class TeamBad:
    members: list = []   # wrong

a = TeamBad()
b = TeamBad()
a.members.append("Aman")
print("Bad A:", a.members)  # ['Aman']
print("Bad B:", b.members)  # ['Aman']<- shared!






