#? Copy Dictionary

#* 1. Direct Assignment (=) – Shallow Reference

# original = {"x": 1, "y": 2}
# copy_ref = original

# copy_ref["x"] = 99
# print(original)
# print(copy_ref)


#* Using .copy() Method – Shallow Copy

# original = {"x": 1, "y": 2}
# original = {"x": 1, "y": {"a": 11, "b": 12}}

# copy = original.copy()

# copy["y"]["a"] = 99
# print(original)
# print(copy)


#* Using dict() constructor – Shallow Copy

# original = {"x": 1, "y": 2}

# copy = dict(original)
# copy["y"] = 99

# print(original)
# print(copy)

#* Using copy.deepcopy() Method – Deep Copy


# original = {"x": 1, "y": {"a": {"c":13, "d":14}, "b": 12}}

# import copy

# deep_copy = copy.deepcopy(original)
# deep_copy["y"]["a"]["d"] = 99

# print(original)
# print(deep_copy)
