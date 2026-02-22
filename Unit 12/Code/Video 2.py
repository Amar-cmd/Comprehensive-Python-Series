#! Opening File
# file = open("test", "r")
# print(file)
#
# ! Closing File
# file.close()

#! Right way of opening file: Using 'with'
# with open("test", "r") as file:
#     # code logic
#     pass
# file automatically closed here

#! Reading File
# with open('test', 'r') as file:
    # content = file.read()
    # content = file.readline()
    # content = file.readlines()
    # print(content)


#! Writing to a File

# lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
#
# with open('parent/test', 'a') as file:
#     file.writelines(lines)












