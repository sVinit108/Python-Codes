'''If we want multiple and independent "constructors", we can use class methods. 
They are usually called factory methods. 
It does not invoke the default constructor __init__.In the above example, we split the string based on the "-" operator. 
We first create a class method as a constructor that takes the string and split it based on the specified operator. 
For this purpose, we use a split() function, which takes the separator as a parameter. 
This alternative constructor approach is useful when we have to deal with files containing string data separated by a separator.'''

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod              
    def from_dash(cls, string): # this class method will take a string and convert it into an obj, thus it can be used as na alternative constructor.
        #params = string.split("-")
        #print(params)
        #return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.from_dash("Karan-480-Student")


