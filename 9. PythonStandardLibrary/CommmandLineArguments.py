# To pass command line arguments in python terminal
import sys
print(sys.argv)
if len(sys.argv) == 1:
    print("USAGE: python CommmandLineArguments.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)
