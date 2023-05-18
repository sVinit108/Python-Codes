class Employee:
    no_of_leaves = 8           # attribute of the class Employee
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

print(harry.no_of_leaves)      
print(harry.__dict__)
harry.no_of_leaves = 9   # this wont change the class attribute but will create a new instance variable of the obj i.e attribute(instance) of harry.
print(harry.__dict__)
print(harry.no_of_leaves)
print(Employee.no_of_leaves)      

print(Employee.no_of_leaves)      
print(Employee.__dict__)
Employee.no_of_leaves = 9    # this will change the class attribute 
print(Employee.__dict__)
print(Employee.no_of_leaves)
 
# we cannot change an attribute of a class through an obj , we will have do it using class only

# Another Example
class Employee1:
  companyName = "Apple"
  noOfEmployees = 0
  def __init__(self, name):
    self.name = name
    self.raise_amount = 0.02
    Employee1.noOfEmployees +=1
  def showDetails(self):
    print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

# Employee.showDetails(emp1)
emp1 = Employee1("Harry")
emp1.raise_amount = 0.3
emp1.companyName = "Apple India" 
emp1.showDetails()
Employee1.companyName = "Google"
print(Employee1.companyName)

emp2 = Employee1("Rohan")
emp2.companyName = "Nestle"
emp2.showDetails()
