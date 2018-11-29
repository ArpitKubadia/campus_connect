class Employee:
    raise_amount=1.04

    def apply_raise(self):
        self.pay=self.pay*self.raise_amount

    def __init__(self,name,pay):
        self.name=name
        self.pay=pay

emp_1=Employee('Corey',50000)
emp_2=Employee('John',40000)
emp_1.raise_amount=1.03
Employee.raise_amount=1.02
print(emp_1.raise_amount)
print(emp_2.raise_amount)