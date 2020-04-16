from pathlib import Path
from time import ctime
import shutil
path = Path("8-Modules/Testing.py")
target = Path()  # Path() means current directory
# path.exist()
# path.rename("TestingRe.txt")
# path.unlink() # Deletes File
print(path.stat())  # Gives information about file. All time info is in seconds from
# 1st Jan 1970
print(ctime(path.stat().st_ctime))  # Prints human readable infor(time)
# path.read_bytes()  # Content of file as bytes object for binary representation of data
# path.read_text()  # Returns content of file as string
# path.write_text("Writing")  # Write in file
# path.write_bytes()  # Write in byte mode

# To Copy file
shutil.copy(path, target)
