class Employee:
    company='Google' # comapany is the attr of the class
    def getAge(self): # self can take both class and object attr
        #print('Salary is 100k')
        print(f'age is: {self.age} and company is {self.company} ')
vinit=Employee()
vinit.age=30 # age is an attr of the object 
vinit.getAge()  # this is line is converted to --> Employee.getSalary(vinit)



