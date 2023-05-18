class C2dvec:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def __str__(self):
        return (f'{self.i}i + {self.j}j')
class C3dvec(C2dvec):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def __str__(self):
        return (f'{self.i}i + {self.j}j + {self.k}k')
v2d=C2dvec(1,3)
v3d=C3dvec(1,2,3)
print(v2d)
print(v3d)