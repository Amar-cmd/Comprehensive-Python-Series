#? Dictionary Methods

#* 1. Access & Iteration

#! 1.1. .get()
# person = {"name": "Amit", "age": 25}
# print(person.get("name"))
# print(person.get("gender", "N/A"))


#! 1.2. .items()
# data = {"x": 10, "y": 20}
# print(list(data.items()))
# for key, value in data.items():
#     print(key, value)


#! 1.3. .keys()

# data = {"x": 10, "y": 20}
# print(data.keys())
# for key in data.keys():
#     print(key)


#! 1.4. .values()

# data = {"x": 10, "y": 20}
# print(data.values())
# for value in data.values():
#     print(value)


#! 1.5. .setdefault()

# user = {"username": "amit123"}
# print(user.setdefault("username"))
# print(user.setdefault("email", "not provided"))
# print(user)


#* 2. Access & Iteration

#! 2.1. .update()

# info = {"name": "Raj", "age": 30}
# print(info)
# info.update({"age": 31, "city": "Mumbai"})
# print(info)


#! 2.2. .pop()

# marks = {"Math": 90, "English": 85}
# print(marks.pop("Math"))
# print(marks)
# print(marks.pop("Science", "Not Available"))


#! 2.3. .popitem()

# colors = {"red": "#f00", "green": "#0f0"}
# print(colors.popitem())
# print(colors)


#! 2.4. .clear()

# config = {"theme": "dark", "font": "Arial"}
# print(config)
# config.clear()
# print(config)


#! 2.5. .fromkeys()

# fields = ["name", "email", "phone"]
# new = dict.fromkeys(fields, "Not Provided")
# print(new)


#* 3. Utility

#! 3.1. .copy()

# original = {"a": 1, "b": 2}
# duplicate = original.copy()
# duplicate["a"] = 99
# print(original)
# print(duplicate)







