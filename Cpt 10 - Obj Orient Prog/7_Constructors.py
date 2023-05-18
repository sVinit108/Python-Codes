class Employee:
    company = 'Google'  # comapany is the attr of the class

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        print('Employee is created')

    def Details(self):
        print(f'Name is {self.name}')
        print(f'Ageis {self.age}')
        print(f'Salary is {self.salary}')

    def getAge(self, a):  # self can take both class and object attr
        print(f'age is: {self.age} and company is {self.company}\n{a}')

    @staticmethod
    def greet():
        print('Good morning sir')
# vinit=Employee()
# vinit.age=30 # age is an attr of the object
# vinit.getAge('Thanks!')  # this is line is converted to --> Employee.getSalary(vinit)
# vinit.greet() # @staticmethod for - Employee.getSalary() and not Employee.greet(vinit)


vivaan = Employee('Vivaan', 18, 100)
# since detail is a method , we have to add a parenthesis.
vivaan.Details()
# since company is an attr & not a method , we don't have to add a parenthesis.
print(vivaan.company)
