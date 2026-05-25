#! +------------------+
#! |  File Organizer  |
#! +------------------+

from pathlib import Path
import shutil

folder_path = input("Enter your folder path: ")

folder = Path(folder_path)

if not folder.exists():
    print("Folder doesn't exist")
elif not folder.is_dir():
    print("Folder is not a directory")
else:
    for file in folder.iterdir():
        if file.is_file():
            extention = file.suffix.lower()

            if extention == "":
                folder_name = "No_extension"
            else:
                folder_name = extention[1:].upper()

        destination_folder = folder / folder_name
        destination_folder.mkdir(parents=True, exist_ok=True)

        destination = destination_folder / file.name
        shutil.move(str(file), str(destination))

print("File Organized successfully")












