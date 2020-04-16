from pathlib import Path

path = Path("8-Modules")
# path.exists() # Check existense
# path.mkdir() # Make directory
# path.rmdir()  # Remove directory
# path.rename() # Rename directory

print(path.iterdir())  # Gives the list of files and directories in this path
# Above we get a generator object.
for p in path.iterdir():
    print(p)

# We can convert generator object to list using list comprehension operator

paths = [p for p in path.iterdir()]
print(paths)

paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)

# The above doesnt search by pattern and doesnt search recursively. For that we use
# glob() as follows:

py_files = [p for p in path.glob("*.py")]  # By pattern
print(py_files)

py_files = [p for p in path.rglob("*.py")]
print(py_files)
