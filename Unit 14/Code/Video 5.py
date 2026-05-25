#! Pathlib
from pathlib import Path

#? Creating a Path
# p1 = Path("data/file.txt")
# print(p1)

# Windows-style absolute path (raw string)
# p2 = Path(r"C:\Users\Amar\doc")
# print(p2)

# Linux/mac absolute path
# p3 = Path("/home/amar/doc")
# print(p3)

#? Current working directory

# cwd = Path.cwd()
# print(cwd)

#? Home directory
# home = Path.home()
# print(home)


#? Joining paths

# base = Path("project")
# file_path = base / "data" / "input.txt"
# print(file_path)


#? Checking path properties

# p = Path("project/data/input.txt")
#
# # Does it exist?
# print(p.exists())
#
# # Is it a file or folder?
# print(p.is_file())
# print(p.is_dir())
#
# # Absolute path
# print(p.resolve()) # full absolute path (also normalizes)
# print(p.absolute()) # absolute without resolving symlinks (behavior differs)

#? Useful parts of a path

# p = Path("project/data/input.txt")
#
# print(p.name)
# print(p.stem)
# print(p.suffix)
# print(p.suffixes)
# print(p.parent)
# print(p.parents)
# print(list(p.parents))

#? Changing file name / extension

# p = Path("data/input.txt")
# new_p = p.with_name("output.txt")
# print(new_p)
#
# # Change suffix (extension)
# new_p = p.with_suffix(".csv")
# print(new_p)

#? Listing files and folders

# # List immediate contents
# folder = Path(r"D:\python\Unit 14\Code")
# # folder.iterdir()
#
# for item in folder.iterdir():
#     # print(item)
#     if item.is_file():
#         print(item.name)


#? Pattern searching

# folder = Path(r"D:\python\Unit 14\Code")

# for item in folder.glob("*.txt"):
#     print(item)

# for item in folder.rglob("*.txt"):
#     print(item)


#? Renaming & Deleting

# p = Path(r"D:\python\Unit 14\Code\1.txt")
# p.rename("new.txt")


# p = Path(r"D:\python\Unit 14\Code\new.txt")
# p.unlink(missing_ok=True)

# p = Path(r"D:\python\Unit 14\Code\Empty")
# p.rmdir()


#? Working with relative vs absolute paths safely

# BASE_DIR = Path(__file__).resolve().parent
# datafile = BASE_DIR / "data" / "input.txt"
# print(datafile)

