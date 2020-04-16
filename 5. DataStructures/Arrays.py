# Arrays are used instead of lists only when there is a huge number of data
from array import array
# First parameter in array() is typecodes for example i for int etc.
# List of type codes can be found on internet
numbers = array("i", [1, 2, 3])
# We can operate on arrays in same way as we do on strings for example
numbers.append(4)
numbers.pop(3)
# In array, each object should be of same type which is specified by typecode while
# making arrays
# Arrays should be used only when a large data is used and performance issues are
# experienced. Else lists and tuples can be used.
