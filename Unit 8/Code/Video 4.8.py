#? Sets Methods

#* 1. Adding Elements

# 1.1 .update()
# s = {1, 2, 3}
# s.update([4, 5, 6])
# print(s)


# 2.2 .add()
# s = {1, 2, 3}
# s.add(4)
# s.add((5, 6))

# print(s)


#* 2. Removing Elements

# 2.1 .discard()
# s = {1, 2, 3}
# s.discard(3)
# print(s)

# s.discard(5)
# print(s)


# 2.2 .remove()
# s = {1, 2, 3}

# s.remove(3)
# print(s)

# s.remove(5)
# print(s)


# 2.3 .pop()
# s = {1, 2, 3}
# s = set()

# s.pop()
# print(s)


# 2.4 .clear()
# s = {1, 2, 3}
# s.clear()
# print(s)


#* 3. Set Operations

# 3.1 .union()

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# print(s1.union(s2))


# 3.2 .intersection()

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# print(s1.intersection(s2))


# 3.3 .difference()

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# print(s1.difference(s2))


# 3.4 .symmetric_difference()

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# print(s1.symmetric_difference(s2))


# 3.5 .intersection_update()

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# s2.intersection_update(s1)
# print(s2)


# 3.6 .difference_update()

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# s1.difference_update(s2)
# print(s1)


# 3.7 .symmetric_difference_update()

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# s1.symmetric_difference_update(s2)
# print(s1)



#* 4. Relationship

# 4.1 issubset()

# s1 = {1, 2}
# s2 = {1, 2, 3, 4}
# print(s1.issubset(s2))


# 4.2 issuperset()

# s1 = {1, 2, 3, 4}
# s2 = {2, 3}
# print(s2.issuperset(s1))


# 4.3 isdisjoint()
# s1 = {1, 2, 3, 4}
# s2 = {4, 5, 6}
# print(s1.isdisjoint(s2))



#* 5. Utility

# 5.1 copy()
# s1 = {1, 2, 3}
# s2 = s1.copy()

# s2.add(4)

# print(s1)
# print(s2)




