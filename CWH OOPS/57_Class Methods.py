class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname   
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod # we cannot change a class attribute using an obj,but using @classmethod we can do so. like self=obj, similiarly cls=class.
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

harry = Employee("Harry", 255, "Instructor")
larry = Employee("larry", 455, "Student")

harry.change_leaves(20)
print(Employee.no_of_leaves)


# Another Example
class Employee1:
  company = "Apple"
  def show(self):
    print(f"The name is {self.name} and company is {self.company}")

  #@classmethod
  def changeCompany(cls, newCompany):
    cls.company = newCompany


e1 = Employee1()
e1.name = "Harry"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee1.company)

# Alternate Method
# Employee.company='Vin'
# print(Employee.company)