# super method is used when we want to run a function from the parent class in the child class.
class person:
    country='India'
    def age(self):
        print('I am 25yrs old')
class employee(person):
    company='Google'
    def salary(self):
        print(f'Salary is {self.salary} ')
    def age(self):
        super().age()
        print('I am 27yrs old')
class programmer(employee):
    company='Microsoft'
    def salary(self):
        print(f'Salary is {self.salary} ')
    def age(self):
        super().age()
        print('I am 30yrs old')
p=person()
p.age()
e=employee()
e.age()
pr=programmer()
pr.age()

# Another Example
class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    super().__init__( name, id)
    self.lang = lang

rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "2345", "Python")
print(harry.name)
print(harry.id)
print(harry.lang)