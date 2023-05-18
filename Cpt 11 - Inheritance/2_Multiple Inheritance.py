class Employee:
    compamy='Google'
    Ecode=123
class Freelance:
    comapny='YT'
    level=1
    def Upgrade(self):
        self.level+=1
class programmer(Employee,Freelance): # in case of same attr in employ and freelan, attr of employ will be given priority as it is written first.
    name='Vinit'
p=programmer()
p.Upgrade()
print(p.level)

# To check order of selection - 
print(programmer.mro())