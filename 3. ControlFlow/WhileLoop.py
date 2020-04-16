number = 100
# below are while loops
# syntax:
# while condition:
#   statement
#   update
while number > 0:
    print(number)
    number //= 2

# another example (below functions like do while in c++)
command = ""
while command != "quit" and command != "QUIT":
    command = input(">")
    print("Echo", command)

# command != "quit" and command != "QUIT" -> this statement can also be written as
# command.lower() != "quit" which converts all text to lower case so no matter how
# the word 'quit' is typed, program always terminates


while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
# the above loop would be infinite since True is always true, so a condition is
# used with break statement to terminate loop. so the above code works exactly like
# the one above it.
