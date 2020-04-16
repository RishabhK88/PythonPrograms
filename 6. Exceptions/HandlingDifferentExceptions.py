try:
    age = int(input("Age: "))
    xfactor = 10/age
except ValueError:
    print("You didn't add valid age.")
except ZeroDivisionError:
    print("You didn't add valid age")
else:
    print("No exceptions encountered")
# The above code is ugly because there is repitition.
# We can write above code as follows ->
try:
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didn't add valid age")
else:
    print("No exceptions encountered")
finally:
    print("Final")
# The above finally clause is always executed even if control is lost in between the
# program. The above clause should be used to close files or other things.
