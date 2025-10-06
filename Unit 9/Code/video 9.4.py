#? Looping Dictionary

#* 1. Default looping

# person = {"name": "Riya", "age": 23, "city":"Pune"}

# for key in person:
#     print(key)
#     print(person[key])


#* 2. Using .keys() method
# for key in person.keys():
#     print(key)
#     print(person[key])


#* 3. Using .values() method
# for value in person.values():
#     print(value)


#* 4. Using .items() method
# print(person.items())

# for key, value in person.items():
#     print(key, value)


#* 5. Using enumerate() function
# for idx, (key, value) in enumerate(person.items(),1):
#     print(f"{idx}. {key} → {value}")


#* 6. Using Dictionary Comprehension

# print(type({key: value for key, value in person.items()})) # ✔️ Creates Dictionary Comprehension
# print(type({(key, value) for key, value in person.items()})) # ❌ Creates Set Comprehension

#todo: extract only string values

# comp = {k: v for k, v in person.items() if type(v) is str}
# print(comp)

#todo: convert string values to upper case

# comp = {k: v.upper() for k, v in person.items() if type(v) is str}
# print(comp)

