class test:
    pass
#print(type(test)) #<class 'type'>

class hi:
    def hello(self):
        return "hello"

def func_hello(self):
    self.xy=1
    return "Function's hello"

test = type('test',(hi,),{"x":5,"func_hello":func_hello}) # 1- internal representation on class, 2- tuple of inherent parent/super class, 3- list of attributes
#print(type(test)) #<class 'type'>

t = test()
print(t.x)
print(t.hello())
print(t.func_hello())
print(t.xy)

class Meta(type):
    def __new__ (self, class_name, bases,attrs) :
        a={}
        for name, val in attrs.items() :
            if name.startswith("__"):
                a[name] = val
            else:
                a[name.upper()] = val
        return type(class_name,bases,a)

class dog(metaclass=Meta):
    x=5
    y=8
    def hello(seLf):
        print ("hi")

d=dog()
print(d.HELLO())