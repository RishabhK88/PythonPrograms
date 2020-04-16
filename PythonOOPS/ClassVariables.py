class Employee1:
    raise_amount = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@gmail.com"
        Employee1.num_of_emp += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay*Employee1.raise_amount)


print(Employee1.num_of_emp)

empl1 = Employee1("Rishabh", "Kumar", 5000)
empl2 = Employee1("Test", "User", 6000)

print(empl1.pay)
empl1.apply_raise()
print(empl1.pay)

print(empl1.raise_amount)
print(Employee1.raise_amount)

print(empl1.__dict__)
print(Employee1.__dict__)

Employee1.raise_amount = 1.05

print(empl1.raise_amount)
print(Employee1.raise_amount)

empl1.raise_amount = 1.06

print(empl1.raise_amount)
print(Employee1.raise_amount)
print(empl2.raise_amount)

print(Employee1.num_of_emp)
