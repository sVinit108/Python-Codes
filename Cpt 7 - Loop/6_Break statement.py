for i in range(10):
    print(i) 
    if i==5:
        break
else:                              # else wont be executed since for loop was stopped in between only.
    print('The loop is completed')
