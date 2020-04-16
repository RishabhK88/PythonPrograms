successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successfull")
        break

# basically break statement is used to break out of a loop. so is the interpreter
# reaches the break statement before loop ends, it will not execute loop any further
# instead execute next line of code after loop ends

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successfull")
        break
else:
    print("Attempted 3 times and failed")
# the above is a for-else loop. the else statement will be executed only if the loop
# is fully executed. if the loop breaks before full execution, else statement is not
# executed
