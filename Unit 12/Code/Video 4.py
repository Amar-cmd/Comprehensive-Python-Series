#! Checking file existence
# import os
# print(os.path.exists('sample')) # ← Checking file existence
# print(os.path.exists('test')) # ← Checking directory existence

#! Making directory

# import os
# os.mkdir('nf') # ← Create a single folder
# os.makedirs('parent/child/subchild', exist_ok=True) # ← Create nested folders

#! Listing directory

# import os
# content = os.listdir("parent")
# print(content)


#! Removing directory

# import os
# os.rmdir('parent') # ← Deletes an empty directory

# import shutil
# shutil.rmtree('parent') # ← Deletes non-empty directories


#! Getting or Changing Current Working Directory

# import os
# print(os.getcwd())
# os.chdir('E:/Python Tutorials/Unit 12')
# print(os.getcwd())
