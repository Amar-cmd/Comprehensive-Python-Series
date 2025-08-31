#? Joining Set

#* 1. Union (|)

# set1 = {1, 2, 3}
# lst = "hello" # Only work with ".union()" method and not with "|" symbol (only works with set)
# set2 = {3, 4, 5}

# 2 ways: | , .union()
# print(set1 | set2) # ✔️
# print(set1 | lst) # ❌
# print(set1.union(set2)) # Works for all





#* 2. Intersection (&)

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
#
# print(set1 & set2)
# print(set1.intersection(set2))

#! NOTE: The & operator joins only sets, unlike intersection(), which works with other data types.


#* 3. Difference (-)

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
#
# print(set1 - set2)
# print(set1.difference(set2))
#
# print(set2 - set1)
# print(set2.difference(set1))

#! NOTE: Order Matters. set1-set2 != set2-set1


#* 4. Symmetric Difference (^)

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
#
# print(set1 ^ set2)
# print(set1.symmetric_difference(set2))



#* Joining Multiple Sets
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5}
# set3 = {4, 5, 6}
# set4 = {4, 7, 8, 9}

#todo: merge elements

# print(set1 | set2 | set3 | set4)
# print(set1.union(set2, set3, set4))

#todo: find common elements
# print(set1 & set2 & set3 & set4)
# print(set1.intersection(set2, set3, set4))







