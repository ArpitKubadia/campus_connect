class Employee:
    def __init__(self,first_name,last_name,pay):
        #self creates a variable for that specific instance
        self.first_name=first_name
        self.last_name=last_name
        self.pay=pay
        self.email=first_name+"."+last_name+"@company.com"

    def getEmail(self):
        return self.email
    def getFullName(self):
        return self.first_name+" "+self.last_name
    def getPay(self):
        return self.pay


emp1=Employee("Mohandas","Gandhi",5000)
print(emp1.getEmail())
print(emp1.getFullName())
print(emp1.getPay())
