class Employee:
    def __init__(self,first_name,last_name,pay):
        self.first_name=first_name
        self.last_name=last_name
        self.pay=pay
        self.email=first_name+"."+last_name+"@company.com"


    def print(self):
        print(emp1.first_name + '\n' + emp1.last_name + '\n' + emp1.email + '\n' + str(emp1.pay))
emp1=Employee("Mohandas","Gandhi",5000)
emp1.print()