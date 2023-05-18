class calculator:
    @staticmethod
    def greet():
        print('Hello')
    def __init__(self,num):
        self.num=num
    def square(self):
        print(f'The sqaure is: {self.num**2}')
    def squareroot(self):
        print(f'The sqaureroot is: {self.num**0.5}')
    def cube(self):
        print(f'The sqaure is: {self.num**3}')
#a=int(input('Enter the number:'))
b=int(input('Enter the number: '))
a=calculator(b)
a.greet()
a.square()
a.squareroot()
a.cube()
