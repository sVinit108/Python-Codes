n1=int(input("Enter the number 1: "))
n2=int(input("Enter the number 2: "))
n3=int(input("Enter the number 3: "))
n4=int(input("Enter the number 4: "))

if(n1>n2):
   f1=n1
else:
    f1=n2
if(n3>n4):
    f2=n3
else:
    f2=n4
if(f1>f2):
    print(str(f1)+' is greatest')
else:
    print(str(f2)+' is greatest')

# if(percentage>=40):
#     if(s1>=33 and s2>=33 and s3>=33):
#          print("You have passed teh exam")
# else:
#     print("You have failed the exam")