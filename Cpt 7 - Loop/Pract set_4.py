a=int(input("Enter the number: "))
prime=True
for i in range(1,a):
    if a%i==0:
        prime=False
        break
if prime:
    print("prime number")
else:
    print('not a prime') 