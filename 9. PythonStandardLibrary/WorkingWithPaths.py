from pathlib import Path

# Declaring Path
Path(r"C:\Program Files\Microsoft")
Path()
path = Path(r"8-Modules\__init__.py")

# Combining Path
Path() / "8-Modules" / "__init__.py"

Path.home()  # returns home directory

path.exists()  # Checks existence of directory
path.is_file()  # To check if path represents file
print(path.name)  # Gives file name
print(path.stem)  # Gives path without extension
print(path.suffix)  # Gives extension
print(path.parent)  # Gives parent of path
# Create a new path object based on existing path
path = path.with_name("file.txt")
# but only change name and extension of file
print(path)
print(path.absolute())  # Absolute value of path
path = path.with_suffix(".txt")
print(path)
# Other members of path class can be found in python documentation
