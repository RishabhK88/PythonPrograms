class Employee1:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@gmail.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)

    def __repr__(self):
        return "Employee1('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp1 = Employee1("Rishabh", "Kumar", 5000)
emp2 = Employee1("Test", "User", 6000)

print(repr(emp1))
print(str(emp1))

print(emp1 + emp2)

print(len(emp1))
