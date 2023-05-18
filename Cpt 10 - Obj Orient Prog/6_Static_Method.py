class Employee:
    company='Google' # comapany is the attr of the class
    def getAge(self,a): # self can take both class and object attr
        #print('Salary is 100k')
        print(f'age is: {self.age} and company is {self.company}\n{a}')
    @staticmethod
    def greet():
        print('Good morning sir')
vinit=Employee()
vinit.age=30 # age is an attr of the object 
vinit.getAge('Thanks!')  # this is line is converted to --> Employee.getSalary(vinit)
vinit.greet() # @staticmethod for - Employee.getSalary() and not Employee.greet(vinit)

#in oops , methods & functions and variables & attr can be used interchangeably