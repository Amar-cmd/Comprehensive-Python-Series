#? Nested Dictionary

#* 1. Creating Nested Dictionary

# students = {
#     "101": {
#         "name": "Ravi",
#         "age": 21,
#         "grade": "A"
#     },
#
#     "102": {
#         "name": "Sara",
#         "age": 22,
#         "grade": "A"
#     }
# }

#* 2. Accessing Elements from Nested Dictionary

# print(students["102"])
# print(students["102"]["grade"])

#* Using .get() method

# print(students.get("1020", "Not available"))


#* 2. Modifying Elements from Nested Dictionary

# students["101"]["grade"] = "A+"
# print(students["101"]["grade"])

# students["102"]["major"] = "CS"
# print(students["102"])

# students["103"] = {"name": "Rajat", "age": 20, "grade": "B+"}
# print(students["103"])

#* 3. Looping Through Nested Dictionaries

# for idx in students:
#     print(idx)
#     print(students[idx])


# for roll, details in students.items():
#     print(f"Roll No: {roll}")
#     for key, value in details.items():
#         print(f"  {key}:{value}")


#* Deleting Items from Nested Dictionaries

# students = {
#     "101": { "name": "Ravi", "age": 21, "grade": "A"},
#     "102": { "name": "Sara", "age": 22, "grade": "A"}
# }
#
# del students["101"]["age"]
# print(students)
#
#
# del students["102"]
# print(students)

