'''
Decorator, as can be noticed by the name, is like a designer that helps to modify a function. 
The decorator can be said to be a modification to the external layer of function, as it does not change its structure. 
A decorator takes a function and inserts some new functionality in it without changing the function itself
There are two ways to write a Python decorator:
We can pass our function to the decorator as an argument, thus defining a function and passing it to our decorator.
 We can simply use the @ symbol before the function we’d like to decorate.
'''

def inner1(func): 
    def inner2(*args,**kwargs):
        print("Before function execution"); 
        func(*args,**kwargs) 
        print("After function execution")    
    return inner2 

@inner1
def function_to_be_used(a,b): 
    print(f"Sum of a+b- {a+b}") 

function_to_be_used(1,2)  

# or
# def function_to_be_used(): 
#     print("This is inside the function")

# function_to_be_used = inner1(function_to_be_used)
# function_to_be_used()