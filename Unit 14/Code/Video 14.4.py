import os
# print(os.getcwd())

# os.chdir(r"D:\Python Project\Unit 14")
# print(os.getcwd())


#! Listing Files and Folders

# print(os.listdir(path="."))

# for item in os.listdir(path="."):
#     print(item)


#! Creating and Removing Directories

# os.mkdir("notes")
# os.makedirs("projects/python/os_module", exist_ok=True)

# os.rmdir("projects")

# import shutil
# shutil.rmtree("projects")


#! File/ Folder Existence Checks

# print(os.path.exists("notes"))
# print(os.path.isfile("data.csv"))
# print(os.path.isdir("projects"))


#! Path Handling

# path = os.path.join("projects", "python", "app.py")
# print(path)
#
#
# file_path = r"C:\Users\Amar\test\data.csv"
# print(os.path.basename(file_path))
# print(os.path.dirname(file_path))
# print(os.path.splitext(file_path))


#! Renaming and Deleting Files

# os.rename("notes.txt", "new notes.txt")
# os.remove("new notes.txt")


#! File Metadata

# size = os.path.getsize("Video 14.4.py")
# print(size/1024)
# print(os.path.getmtime("Video 14.4.py"))
# print(os.path.getatime("Video 14.4.py"))
# print(os.path.getctime("Video 14.4.py"))
#
# print(os.stat("Video 14.4.py"))
















