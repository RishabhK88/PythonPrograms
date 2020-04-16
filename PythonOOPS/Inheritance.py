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


class Developer(Employee1):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee1):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def AddEmployee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def RemoveEmployees(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def PrintEmp(self):
        for emp in self.employees:
            print(f"-->{emp.fullname()}")


dev1 = Developer("Rishabh", "Kumar", 5000, "python")
dev2 = Developer("Test", "User", 6000, "java")

mngr1 = Manager("Sue", "Smith", 90000, [dev1])
# print(dev1.email)
# print(help(Developer))

# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)

# print(dev1.email)
# print(dev1.prog_lang)

print(mngr1.email)
mngr1.PrintEmp()
mngr1.AddEmployee(dev2)
mngr1.PrintEmp()
mngr1.RemoveEmployees(dev1)
mngr1.PrintEmp()


print(isinstance(mngr1, Manager))
print(isinstance(mngr1, Employee1))
print(isinstance(mngr1, Developer))

print(issubclass(Manager, Employee1))
print(issubclass(Developer, Manager))
