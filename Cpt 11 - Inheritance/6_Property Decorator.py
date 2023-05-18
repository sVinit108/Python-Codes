class Employee:
    comapany='Bharat Gas'
    salary=5000
    salaryBonus=100
    # Totalsalary=5100
    @property                               # also known as getter method
    def Totalsalary(self):
        return self.salary+self.salaryBonus

    @Totalsalary.setter
    def Totalsalary(self,val):
        self.salaryBonus = val - self.salary

a=Employee()
print(a.Totalsalary)
a.Totalsalary=5500
print(a.salary)
print(a.salaryBonus)
print(a.Totalsalary)

# Another Example
class Myclass:
    def __init__(self,val):
        self.val = val

    def show(self):
        print(self.val)

    @property
    def multi(self):
        return 10*self.val
    
    @multi.setter
    def multi(self,new_val):
        self.val = new_val

obj = Myclass(10)
obj.show()
print(obj.multi)
obj.multi=12
print(obj.multi)