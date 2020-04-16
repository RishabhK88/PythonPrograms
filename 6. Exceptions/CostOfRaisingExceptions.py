# Raising exceptions comes with a cost of runtime. So raising exceptions is not
# advisable. We can calculate running time of python programming by importing timeit
from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less")
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass 
    
"""
print("Firstcode:", timeit(code1, number=10000))
# The above function will execute python code 10000 times and give the run time.

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age


x_factor = calculate_xfactor(-1)
if x_factor == None:
    pass
    
"""
print("Secondcode:", timeit(code2, number=10000))

# On running the program it will be observed that time required to run first program
# is almost 4 to 5 times as much required to run second code. So raising exceptions
# causes lot of time consumption.

# We see this difference in time only because we are running the code 10000 times.
# No difference in time is observed if program is executed twice, since it is a
# small program. In large program, where build time is significant, we should
# raise exceptions only if we have to.
