# Escape squences are used as \e where e is the character to be printed
# they are used when a character is to be added and syntax doesnt allow it
# For example if there is to be a quotation mark in string, it is not possible
# because quotation marks will end the string right there, so we use escape
# sequence -> \" like given below
course = "Python \" Programming"
print(course)
# so back slash(\) is not printed
# Following are some escape sequences
# \"
# \'
# \\ -> for backslash
# \n -> to add a new line
print("Python\nProgramming")
