def fizz_buzz(input):
    if input % 3 == 0 and input % 5 != 0:
        return "Fizz"
    elif input % 5 == 0 and input % 3 != 0:
        return "Buzz"
    elif input % 5 == 0 and input % 3 == 0:
        return "FizzBuzz"
    else:
        return input


print(fizz_buzz(6))
print(fizz_buzz(10))
print(fizz_buzz(15))
print(fizz_buzz(7))
