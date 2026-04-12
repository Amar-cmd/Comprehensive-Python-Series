#! Dataclass

#* Without Dataclass
# class Student:
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll
#
#     def __repr__(self):
#         return f"Student(name = {self.name}, roll= {self.roll})"



#* With Dataclass
# from dataclasses import dataclass
#
# @dataclass
# class Student:
#     name: str
#     roll: int

#* Default Values

# from dataclasses import dataclass
#
# @dataclass
# class Student:
#     name: str
#     roll: int = 1
#
# s = Student("Ravi")
# print(s.roll)


#* Default Values - () or {}

#! WRONG:
# from dataclasses import dataclass
#
# @dataclass
# class TeamBad:
#     members: list = []

#* CORRECT:
# from dataclasses import dataclass, field
#
# @dataclass
# class TeamGood:
#     members: list = field(default_factory=list)
#
# x = TeamGood()
# y = TeamGood()
#
# x.members.append("Aman")
# print(x.members)
# print(y.members)



#* __post_init__():

# from dataclasses import dataclass
#
# @dataclass
# class User:
#     name: str
#     age: int
#
#     def __post_init__(self):
#         if self.age < 0:
#             raise ValueError("Age cannot be negative")
#
# u = User("Amar", -20)
# print(u)









