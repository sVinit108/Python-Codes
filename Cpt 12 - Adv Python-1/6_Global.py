a=10                           # Global variable
def func1():
    global a
    print(f'1st line: {a}')
    a=8                        # Local variable if global is not used
    print(f'2nd line: {a}')
func1()
print(f'3rd line: {a}')

