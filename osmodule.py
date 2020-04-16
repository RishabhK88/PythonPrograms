import os
print(dir(os))
print(os.getcwd())  # to get current working directory
os.chdir("C://")  # change directory
print(os.getcwd())
os.chdir("C://Rishabh/Python")
print(os.getcwd())
print(os.listdir())  # files and folders in current path
print(os.listdir("C://"))  # files and folders in specified path
# os.mkdir("New")  # Makes new folder
# os.makedirs("New1/New2")
# makes directory new 1 and in it a sub directory new2
# os.rename("Rishabh.txt", "HeyRishabh.txt")  # rename
print(os.environ.get("Path"))  # to get a environment variable
print(os.path.join("C://", "HeyRishabh.txt"))  # to join paths

print(os.path.exists("C://"))  # Check existence of path
print(os.path.isfile("C://"))  # check existence of files
