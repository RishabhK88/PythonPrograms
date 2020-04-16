from Sales import calc_shipping, calc_tax

# We can also use multiple objects using "import *" but it is not advisable since
# the module may contain a lot of objects that may override the objects with same
# name in current module

# We can also import entire module as an object by "import Sales" and then access
# its objects by Sales.calc_shipping()

calc_shipping()
calc_tax()
