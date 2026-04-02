#! Inheritance

# class Animal:
#     def speak(self):
#         print("Some sound")
#
# class Dog(Animal):
#     pass


#! Multiple Inheritance

# class Dad:
#     def dad_trait(self):
#         print("Hardworking Quality")
#
# class Mom:
#     def mom_trait(self):
#         print("Very Smart")
#
# class Kid(Dad, Mom):
#     pass
#
#
# d = Kid()
#
# d.dad_trait()
# d.mom_trait()


#! Multilevel Inheritance
# class Animal:
#     def eat(self):
#         print("Animal is eating")
#
# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")
#
# class Puppy(Dog):
#     def play(self):
#         print("Puppy is playing")
#
# p = Puppy()
#
# p.eat()
#
# p.bark()
#
# p.play()


#! Hierarchical Inheritance

# class Animal:
#     def eat(self):
#         print("Animal is eating")
#
# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")
#
# class Cat(Animal):
#     def meow(self):
#         print("Cat is meowing")
#
# d = Dog()
# c = Cat()
#
# d.eat()
# d.bark()
# c.eat()
# c.meow()





#! Hybrid Inheritance

# class Person:
#     def show_person(self):
#         print("I am a person")
#
# # Hierarchical inheritance (two children from Person)
# class Student(Person):
#     def show_student(self):
#         print("I am a student")
#
# class Teacher(Person):
#     def show_teacher (self):
#         print("I am a teacher")
#
# class Assistant(Student, Teacher):
#     def show_assistant(self):
#         print("I am an assistant")
#
#
# ta = Assistant()
#
# ta.show_person()
# ta.show_student()
# ta.show_teacher()
# ta.show_assistant()



#! super() in Inheritance

# class Parent:
#     def __init__(self, msg):
#         self.msg = msg
#
# class Child(Parent):
#     def __init__(self, msg):
#         super().__init__(msg)     # calls Parent.__init__
#
# c = Child("Hello")
# print(c.msg)   # Hello



