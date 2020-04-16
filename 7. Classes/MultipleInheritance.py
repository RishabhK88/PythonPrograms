class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):
    pass


manager = Manager()
manager.greet()

# In above code, Employee Greet will be printed because it is above class Person.
# The first function encountered will be executed
