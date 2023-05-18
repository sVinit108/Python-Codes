class Employees:
    company='Microsoft'
    def __init__(self,name,no,address,age):
        self.name=name
        self.no=no
        self.address=address
        self.age=age
        print('Welcome to the database!')

    def Details(self):
        print(f'''
        Name = {self.name} 
          no = {self.no} 
     address = {self.address}
         age = {self.age}''')
  
harry=Employees('Harry',2,'USA',30)
harry.Details()

vinit=Employees('vinit',2,25,'India')
vinit.Details()

vivaan=Employees('Vivaan',3,23,'India')
vivaan.Details()

