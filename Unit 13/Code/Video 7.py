#! Abstract Base Class (ABC)
# from abc import ABC, abstractmethod
#
# class Greet(ABC):
#     @abstractmethod
#     def say_hello(self):  # Abstract method
#         pass
#
# class English(Greet):
#     def say_hello(self):
#         return "Hello!"
#
# g = English()
# print(g.say_hello())


#! Abstract Method

# from abc import ABC, abstractmethod
#
# class Vehicle(ABC):
#     @abstractmethod
#     def honk(self):
#         pass  # Abstract method, no implementation here
#
#     def steer_left(self):
#         return "Left"
#
# class Car(Vehicle):
#     def honk(self):
#         return "Honk!!!"
#
# c = Car()
#
# print(c.honk())
# print(c.steer_left())


#! Abstract Properties

# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#
#     @property
#     @abstractmethod
#     def area(self):
#         pass
#
# class Square(Shape):
#     def __init__(self, side):
#         self.__side = side
#
#     @property
#     def area(self):
#         return self.__side ** 2  # Concrete implementation
#
# s = Square(5)
# print(s.area)


#! Abstract Class Instantiation Rules

# from abc import ABC, abstractmethod
#
# class Vehicle(ABC):
#     @abstractmethod
#     def honk(self):
#         pass  # Abstract method, no implementation here
#
# Vehicle = Vehicle()












