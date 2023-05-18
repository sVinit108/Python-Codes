s1=int(input("Enter your Physics marks: "))
s2=int(input("Enter your Chemistry marks: "))
s3=int(input("Enter your Maths marks: "))
percentage=(s1+s2+s3/3)
if(percentage>=40):
    if(s1>=33 and s2>=33 and s3>=33):
        print("You have passed the exam")
    else:
        print("You have failed the exam")
else:
    print("You have failed the exam")