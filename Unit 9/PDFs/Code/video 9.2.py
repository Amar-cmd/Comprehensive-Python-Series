#? Creating Dictionary

#* 1. Using curly braces {}

# employee = {"name": "Amar", "age" : 18, "Department": "HR"}
# print(employee)
# print(type(employee))



#* 2. Using dict()

# employee = dict(name = "Amar", age = 18, department = "HR")
# print(employee)
# print(type(employee))



#* 3. Using zip()

# keys = ["id", "name", "score"]
# values = [101, "arjun", 89]
#
# record = dict(zip(keys, values))
# print(record)


#? Accessing Element in Dictionary

#* 1. Using Square Brackets []

# student = {"name": "Amar", "age": 20, "course": "Python"}

# print(student["ages"])


#* 2. Using .get() method

# print(student.get("ages", "N/A"))


#* 3. Using .keys(), values, items() method

# student = {"name": "Amar", "age": 20, "course": "Python"}

#! 3.1 Using .keys()

# for key in student.keys():
#     print(key)

#! 3.2 Using .values()
# for values in student.values():
#     print(values)

#! 3.3 Using .items()
# for keys, values in student.items():
#     print(keys, "→", values)



# ? Modifying Element in Dictionary

# book = {"title": "1984", "author": "Orwell", "price": 350}

# print(book)

#* Using square brackets []
# book["price"] = 299
# print(book)

#* Using .update() method
# book.update({"price": 499, "pages": 328})
# print(book)

#* Inserting new key-value pair
# book["pages"] = 328
# print(book)


# ? Removing Elements from Dictionary

# car = {"brand": "Toyota", "model": "Corolla", "year": 2020}

#* Using pop()
# remove = car.pop("years", "error")
# print(car)
# print(remove)


#* Using popitem()
# car.popitem()
# print(car)


#* Using clear()
# car.clear()
# print(car)


#* Using del keyword
# del car["model"]
# print(car)




