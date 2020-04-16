# in below code by is an optional parameter i.e. it is given a default value
# all default parameters should be after the rest of them, so no parameters can
# be declared after optional parameter


def increment(number, by=1):
    return number + by


print(increment(number=2, by=1))
