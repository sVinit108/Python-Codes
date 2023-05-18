class Employee:
    company = 'Google'
vinit = Employee()
vivaan = Employee()
vinit.salary = 300
vivaan.salary = 100
print(vinit.company)
print(vivaan.company)
Employee.company = 'Youtube'
print(vinit.company)
print(vivaan.company)
print(vinit.salary)
print(vivaan.salary)
