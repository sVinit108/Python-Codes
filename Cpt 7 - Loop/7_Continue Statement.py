for i in range(10):
    if i==5:
        continue # when i=5,it wont print 5 but will proceed with the loop
    print(i)
else:
    print("The loop is completed")