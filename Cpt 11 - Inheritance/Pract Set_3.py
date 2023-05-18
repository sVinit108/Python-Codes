class Employee:
    Company='Google'
    Salary=1000
    increment=1.5
    @property
    def Totalsalary(self):
        return self.Salary*self.increment
    @Totalsalary.setter
    def Totalsalary(self,val):
        self.increment=val/self.Salary
a=Employee()
a.Totalsalary=200
print(a.Salary)
print(a.increment)
print(a.Totalsalary)

