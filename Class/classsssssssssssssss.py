"""
class ParentClass:
    a = 10
    b = 20
    def get_sum(self):# this is the super class 
        print('Inside parent class')
        return self.a + self.b
class ChildClass(ParentClass):
    def get_sum(self):
        print('Inside child class')# this is sub class
        print(f'a = {self.a}, b = {self.b}')
        return super().get_sum()
c = ChildClass()
print(c.get_sum())
"""
# simple inhertens
class pettrans:
    def __init__(self,a=0):
        self.b=a
        self.a=a
class small (pettrans):    
    def A(self,a):
        for row in range(a):
            for col in range(a+a):
                if (row+col==a-1)or (col==row+a-1)or (row==a//2 and col>a//2-1 and col<a+a//2): #col!=b-1 and col!=b-2 and col!=b-3 and col!=b-4 and col!=b-5 ) and col<4:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def B(self,b):
        for row in range(b):
            for col in range(b):
                if (col==0)or(row==0 and 2<b and col!=b-1 and col!=b-2)or(row==b-1 and 2<b and col!=b-1 and col!=b-2)or(col==b-2 and row!=0 and row!=b-1 and row!=b//2)or(row==b//2 and col!=b-1 and col!=b-2 ):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def C(self,b):
        for row in range(b):
            for col in range(b):
                if (col==0 and row!=0 and row!=b-1)or(row==0 and col!=0)or(row==b-1 and col!=0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def D(self,b):
        for row in range(b):
            for col in range(b):
                if (col==0)or(row==0 and 2<b and col!=b-1 and col!=b-2)or(row==b-1 and 2<b and col!=b-1 and col!=b-2)or(col==b-2 and row!=0 and row!=b-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        
    def E(self,a):
        for row in range(a):
            for col in range(a):
                if (row==0) or (row==a//2 )or (row==a-1)or(col==0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        
    def F(self,a):
        for row in range(a):
            for col in range(a):
                if (row==0 and col<a-2) or (row==a//2-1 and col<a-2)or(col==0 ):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def G(self,b):
        for row in range(b):
            for col in range(b):
                if (col==0 and row!=0 and row!=b-1 and row!=b-2)or(row==0 and col!=0)or(row==b-2 and col!=0)or(col==b-1 and row>b//2-1)or(row==b//2 and col>1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def H(self,a):
        for row in range(a):
            for col in range(a):
                if (row==a//2) or (col==0) or (col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def I(self,a):
        for row in range(a):
            for col in range(a):
                if (col==a//2) or(row==0)or(row==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()            
    def J(self,a):
        for row in range(a):
            for col in range(a):
                if (col==a//2) or(row==0)or(row==a//2+col):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()            
    def K(self,a):
        for row in range(a):
            for col in range(a):
                if (col==0)or (row==col+a//2-1)or(row+col==a-a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
            
            
    def L(self,a):
        for row in range(a):
            for col in range(a):
                if (col==0)or(row==a-1 and col!=a-1 and col!=a-2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def M(self,a):
        c=a+a
        b=c-2
        for row in range(a):
            for col in range(b):
                if (col==0)or(row==col)or(row+col==b>8-1)or (col==b-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def N(self,a):
        for row in range(a):
            for col in range(a):
                if (col==0)or(row==col)or (col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def O(self,a):
        for row in range(a):
            for col in range(a):
                if (row==0 and col!=0 and col!=a-1) or (row==a-1 and col!=0 and col!=a-1) or (col==0 and row!=0 and row!=a-1) or (col==a-1 and row!=0 and row!=a-1 ):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    def P(self,a):
        for row in range(a+5):
            for col in range(a):
                if (row==0  and col!=a-1)or (row==a-1 and col!=a-1) or (col==0  and row!=a-1)or (col==a-1 and row!=0 and row<=a-1 and row!=a-1 ):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    def Q(self,a):
        for row in range(a):
            for col in range(a):
                if (row==0 and col!=0 and col!=a-2 and col!=a-1) or (row==a-2 and col!=0 and col!=a-1) or (col==0  and row!=0 and row<a-2) or (col==a-2 and row!=0 and row!=a-1)or (row==a-3 and col==a-3 ) or(row==a-4 and col==a-4)or(row==a-1 and col==a-1):
                     print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def R(self,a):
        for row in range(a+a):
            for col in range(a):
                if (row==0  and col!=a-1)or (row==a-1 and col!=a-1) or (col==0  and row!=a-1)or (col==a-1 and row!=0 and row<=a-1 and row!=a-1)or(row==col+a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def S(self,a):
        for row in range(a):
            for col in range(a):
                if (row==0) or (row==col ) or (row==a-1):
                     print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    def T(self,a):
        for row in range(a):
            for col in range(a):
                if (col==a//2) or(row==0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def U(self,a):
        for row in range(a):
            for col in range(a):
                if (col==0 and row!=a-1)or (row==a-1 and col!=0 and col!=a-1) or(col==a-1 and row!=a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def V(self,a):
        for row in range(a):
            for col in range(a*2+2):
                if (row+col==a+a//2+a%2)or(row==col):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


    def W(self,a):
        for row in range(a):
            for col in range(a+a):
                if (col==0) or(row+col==a-1)or(col==row+a-1)or(col==a+a-2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    def X(self,a):
        for row in range(a):
            for col in range(a):
                if (row+col==a-1) or row==col:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def Y(self,a):
        for row in range(a):
            for col in range(a*2+2):
                if (row==col and col<a-a//2)+(row+col==a-1 and row<a-a//2)or (col==a-a%2-a//2 and row>a//2-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
         
    def Z(self,a):
        for row in range(a):
            for col in range(a):
                if (row==0) or(row+col==a-1)or (row==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()         
         
