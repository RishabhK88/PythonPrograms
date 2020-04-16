class Employee:
    pass


emp1 = Employee()
emp2 = Employee()

print(emp1)
print(emp2)

emp1.first = "Rishabh"
emp1.last = "Kumar"


emp2.first = "Test"
emp2.last = "User"

print(emp1.first)
print(emp2.first)

# Instead of manually setting up variable like these:


class Employee1:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@gmail.com"

    def fullname(self):
        return f"{self.first} {self.last}"


empl1 = Employee1("Rishabh", "Kumar")
empl2 = Employee1("Test", "User")

print(empl1.fullname())
print(Employee1.fullname(empl1))  # THis line and the line above do same thing
print(empl2.fullname())
