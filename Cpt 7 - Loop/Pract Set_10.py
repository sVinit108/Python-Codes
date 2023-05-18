num=int(input("Enter the number: "))
i=1
for i in range(10,0,-1):
  # print(str(num)+'X'+str(i)+ "=" +str(i*num))
  # print(f"{num}X{i}={i*num}")
    print("%sX%s=%s"%(num,i,i*num))