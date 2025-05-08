#? PART - 1
#! Copying List

#* list()
# original_list = [1, 2, 3]
# copied_list = list(original_list)

# copied_list.append(4)

# print(original_list) #1, 2, 3
# print(copied_list) # 1, 2, 3, 4


#* .copy() method
# original_list = [1, 2, 3]
# copied_list = original_list.copy()

# copied_list.append(4)

# print(original_list) #1, 2, 3
# print(copied_list) # 1, 2, 3, 4


#* Slice Notation
# original_list = [1, 2, 3]
# copied_list = original_list[:]
# copied_list.append(4)

# print(original_list) #1, 2, 3
# print(copied_list) # 1, 2, 3, 4


#* Shallow Copy
# original_list = [[1, 2], [3, 4]]

# copy_list = original_list.copy()
# copy_list[0].append(3)

# print(original_list)
# print(copy_list)


#* DEEP COPY
# import copy
# original_list = [[1, 2], [3, 4]]

# copy_list = copy.deepcopy(original_list)
# copy_list[0].append(3)

# print(original_list)
# print(copy_list)

#? PART - 2
# ! Joining List

# * Using '+' Operator
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# joined_list = list1 + list
# print(joined_list)


# * Using .extend() method
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.extend(list2)
# print(list1)


# * Using .append() method
# list1 = ["a", "b", "c"]
# list2 = ["d", "e", "f"]
# for l2 in list2:
#     list1.append(l2)
# print(list1)


# * Using List Comprehension
# list1 = ["a", "b", "c"]
# list2 = ["d", "e", "f"]
# [list1.append(l2) for l2 in list2]
# print(list1)