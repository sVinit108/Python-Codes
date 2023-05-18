'''
All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.
Eg:-
    self.age = age      # public variable

By definition, Private members of a class (variables or methods) are those members which are only accessible inside the class. We cannot use private members outside of class.
In Python, there is no strict concept of "private" access modifiers like in some other programming languages. However, a convention has been established to indicate that a variable or method should be considered private by prefixing its name with a double underscore (__). This is known as a "weak internal use indicator" and it is a convention only, not a strict rule. Code outside the class can still access these "private" variables and methods, but it is generally understood that they should not be accessed or modified.
Eg:-
    self.__age = age      # An indication of private variable
Name mangling in Python is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses. Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively.
Eg:-
    class MyClass:
        def __init__(self):
            self._nonmangled_attribute = "I am a nonmangled attribute"
            self.__mangled_attribute = "I am a mangled attribute"

    my_object = MyClass()

    print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
    print(my_object.__mangled_attribute) # Throws an AttributeError
    print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute

In object-oriented programming (OOP), the term "protected" is used to describe a member (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses. In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_). For example, if a class has a method called _my_method, it is indicating that the method should only be accessed by the class itself and its subclasses.

It's important to note that the single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member. The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) ie. _varName.
Eg:- 
    class Student:
        def __init__(self):
            self._name = "Harry"
        def _funName(self):      # protected method
            return "CodeWithHarry"
    class Subject(Student):       #inherited class
        pass
    obj = Student()
    obj1 = Subject()
    # calling by object of Student class
    print(obj._name)      
    print(obj._funName())     
    # calling by object of Subject class
    print(obj1._name)    
    print(obj1._funName())
'''