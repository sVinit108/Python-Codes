class Employee:
    company='Google'
    def Detials(self):
        print('This is an employee')
    
class programmer(Employee):
    language='Python'
    def get_Language(self):
        print(f'The language is {self.language}')


b=Employee()
b.Detials()
a=programmer()
a.get_Language()
a.Detials()
