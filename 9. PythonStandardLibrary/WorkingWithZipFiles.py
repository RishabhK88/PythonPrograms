from pathlib import Path
from zipfile import ZipFile
with ZipFile("files.zip", "w") as zip:  # "w" is short for "write"
    Path("8-Modules/Testing.py")
    zip.write(Path)

with ZipFile("files.zip") as zip:  # Default mode is read mode
    print(zip.namelist())  # Gives name of all files in zip files
    # To get file info
    info = zip.getinfo("Testing.py")
    print(info.file_size)
    print(info.compress_size)
    # Extracts all files of zip file into "extract" directory
    zip.extractall("extract")
