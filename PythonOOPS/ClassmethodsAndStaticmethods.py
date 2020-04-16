import datetime


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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string):  # using classmethod as contructor
        first, last, pay = emp_string.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


empl1 = Employee1("Rishabh", "Kumar", 5000)
empl2 = Employee1("Test", "User", 6000)
emp_str_1 = "John-Doe-7000"
emp_str_2 = "Steve-Smith-3000"
emp_str_3 = "Jane-Doe-9000"

new_emp1 = Employee1.from_string(emp_str_1)
new_emp2 = Employee1.from_string(emp_str_2)
new_emp3 = Employee1.from_string(emp_str_3)

print(new_emp1.first)


# Employee1.set_raise_amount(1.05)
# print(Employee1.raise_amount)
# print(empl1.raise_amount)
# print(empl2.raise_amount)

my_date = datetime.date(2019, 5, 19)
print(Employee1.is_workday(my_date))
