# Ternary operator can be used instead of if statement
age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)

# Instead of above code the following code can be written which is cleaner
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)
