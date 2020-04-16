try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't add valid age.")
    print(ex)
    print(type(ex))
else:
    print("No exceptions encountered")
# If the ValueError is encountered by program, instead of crashing it will print the
# message in except. Due to the "as ex" it will also give the reason of error.
# The else clause is executed only if no exception is encountered
print("Execution Continues")
