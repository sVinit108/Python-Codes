'''Constructor - the purpose of a constructor is to assign values to the instance variables of different objects. 
We can give the values by accessing each of the variables one by one, but in the case of the constructor, 
we pass all the values directly as parameters. '''
# for more understanding refer video 56, 6:35.

# self can take both class and object attr. 1st priority is given to obj and then to class.

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname   #self.name - its the instances variable i.e attribute of the obj,aname-its 'name' of the argument which we are taking.
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


vinit = Employee("vinit", 255, "Instructor") # when we make construtor we dont have do this *
# *vinit.name = "vinit"
# *vinit.salary = 455
# *vinit.role = "Instructor"

# rohan = Employee()       
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"

print(vinit.salary)

