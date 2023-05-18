class Number:
    def sum(self,a,b):
        self.a=a
        self.b=b
        return a + b
num=Number()
Number.sum(1,2,4)
# num.a=12
# num.b=10
print(num.sum)