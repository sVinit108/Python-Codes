def factorial_recursive(n):
    if n==0 or n==1:
            return 1
    else:
        return n*factorial_recursive(n-1)
n=int(input('Enter the number: '))
print(factorial_recursive(n))
