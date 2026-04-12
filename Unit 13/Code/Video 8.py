#! Polymorphism
#* A. Function Polymorphism (Built-in functions)
# print(len("Hello"))
# print(len([1,2,3,4]))

#* B. Operator Polymorphism (Operator Overloading)
# print(10 + 20)
# print("Hi" + " Amar")
# print([1, 2] + [3, 4])

#* C. Method Polymorphism (Same method name in different classes)
# class Dog:
#     def speak(self):
#         return "Bark"
#
# class Cat:
#     def speak(self):
#         return "Meow"
#
# animals = [Dog(), Cat()]
#
# for a in animals:
#     print(a.speak())

#* D) Method Overriding (Same method name in different classes)
# class Animal:
#     def speak(self):
#         return "Some Sound"
#
# class Dog(Animal):
#     def speak(self):
#         return "Bark"
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow"
#
# print(Animal().speak())
# print(Dog().speak())
# print(Cat().speak())


#* Duck Typing
# class Bike:
#     def start(self):
#         return "bike started"

# class Car:
#     def start(self):
#         return "car started"

# def begin(vehicle):
#     return vehicle.start()

# print(begin(Bike()))
# print(begin(Car()))
