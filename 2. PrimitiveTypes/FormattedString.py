first = "Rishabh"
last = "Kumar"
# Concatenation method(correct but not good code):
full = "Hi, " + first + " " + last
print(full)
# Formatted string method(better to be used):
full = f"Hi, {first} {last}"
print(full)
# Note: The curly brackets can contain any type of variable or even a mathematical
# expression that will be evaluated or even functions such as len()
full = f"{len(first)} {2 + 2}"
print(full)
