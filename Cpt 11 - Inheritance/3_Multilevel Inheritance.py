class person:
    country='India'
    def age(self):
        print('I am 25 yr old')
class employee(person):
    company='Google'
    def salary(self):
        print(f'Salary is {self.salary} ')
    def age(self):
        print('I am 27 yr old')
class programmer(employee):
    company='Microsoft'
    def salary(self):
        print(f'Salary is {self.salary} ')
    def age(self):
        print('I am 30 yr old')
p=person()
p.age()
e=employee()
e.age()
pr=programmer()
pr.age()
