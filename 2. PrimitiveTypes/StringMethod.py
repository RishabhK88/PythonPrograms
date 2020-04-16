course = "Python Programming"
# Functions(methods) specific to strings
# ***Note: The following functions to not make changes in the original string
print(course.upper())
# upper() is used to turn string to upper case
print(course.lower())
# lower() is used to turn string to lower case
print(course.title())
# title() is used to capitalize first letter of each word
print(course.strip())
# strip() is used to deleted space at front and back of string
# lstrip() removes beginning space
# rstrip() removes end space
print(course.find("Pro"))
# find() is used to find the start index of a part or character of the original
# string. if the part or char is not in string, find() returns -1
print(course.replace("P", "J"))
# replace() is used to replace a character or part of string with others
print("Pro" in course)
# in is used to check the existence of a character or sequence of characters
# in string. It returns a boolean i.e. true or false
print("Swift" not in course)
# not in
