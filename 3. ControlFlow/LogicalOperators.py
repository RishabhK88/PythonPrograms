# 3 logical operators in python are and, or and not
# The below code is self explanatory and has different instances of how logical
# operators can be used
high_income = True
good_credit = False
student = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")


if high_income or good_credit:
    print("Eligible")
else:
    print("Not Eligible")


if not student:
    print("Eligible")
else:
    print("Not Eligible")


if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")


# python does a short circuit evaluation. so, in below case if it encounters a true
# it evaluates further otherwise it doesnt, since it is 'and'. so evaluation
# terminates as soon as a false is encountered. If it is 'or' python expects one of
# the values to be true, if it doesnt, then no further evaluation of expression
# takes place
if high_income and good_credit and not student:
    print("Eligible")
else:
    print("Not Eligible")
