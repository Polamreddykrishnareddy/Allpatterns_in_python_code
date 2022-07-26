class capital_alphabets:
    def __init__(self):
        pass
    #A
    def A(self,a):
        b=a+a
        row=0
        while row<a:
            col=0
            while col<b:
                if (row+col==a-1)or (col==row+a-1)or (row==a//2 and col>a//2-1 and col<a+a//2): 
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
    def B(self,b):
        row=0
        while row<b:
            col=0
            while col<b:
                if (col==0)or(row==0 and 2<b and col!=b-1 and col!=b-2)or(row==b-1 and 2<b and col!=b-1 and col!=b-2)or(col==b-2 and row!=0 and row!=b-1 and row!=b//2)or(row==b//2 and col!=b-1 and col!=b-2 ):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
            
    def C(self,b):
        row=0
        while row<b:
            col=0
            while col<b:
                if (col==0 and row!=0 and row!=b-1)or(row==0 and col!=0)or(row==b-1 and col!=0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
    def D(self,b):
        row=0
        while row<b:
            col=0
            while col<b:
                if (col==0)or(row==0 and 2<b and col!=b-1 and col!=b-2)or(row==b-1 and 2<b and col!=b-1 and col!=b-2)or(col==b-2 and row!=0 and row!=b-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
            
    def E(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==0) or (row==a//2 )or (row==a-1)or(col==0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
    def F(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==0 and col<a-2) or (row==a//2-1 and col<a-2)or(col==0 ):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()            
    def G(self,b):
        row=0
        while row<b:
            col=0
            while col<b:
                if (col==0 and row!=0 and row!=b-1 and row!=b-2)or(row==0 and col!=0)or(row==b-2 and col!=0)or(col==b-1 and row>b//2-1)or(row==b//2 and col>1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()           
    def H(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==a//2) or (col==0) or (col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()           
            
    def I(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (col==a//2) or(row==0)or(row==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
    def J(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (col==a//2) or(row==0)or(row==a//2+col):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()            
            
    def K(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (col==0)or (row==col+a//2-1)or(row+col==a-a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()            
            
    def L(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (col==0)or(row==a-1 and col!=a-1 and col!=a-2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()            
            
    def M(self,b):
        row=0
        while row<b:
            col=0
            while col<b+b:
                if (col==0)or(row==col)or(row+col==b+b-2)or(col==b+b-2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()            
    def N(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (col==0)or(row==col)or (col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()

    def O(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==0 and col!=0 and col!=a-1) or (row==a-1 and col!=0 and col!=a-1) or (col==0 and row!=0 and row!=a-1) or (col==a-1 and row!=0 and row!=a-1 ):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
    def P(self,a):
        row=0
        while row<a+5:
            col=0
            while col<a:
                if (row==0  and col!=a-1)or (row==a-1 and col!=a-1) or (col==0  and row!=a-1)or (col==a-1 and row!=0 and row<=a-1 and row!=a-1 ):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
    def Q(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==0 and col!=0 and col!=a-2 and col!=a-1) or (row==a-2 and col!=0 and col!=a-1) or (col==0  and row!=0 and row<a-2) or (col==a-2 and row!=0 and row!=a-1)or (row==a-3 and col==a-3 ) or(row==a-4 and col==a-4)or(row==a-1 and col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()

    def R(self,a):
        row=0
        while row<a+a:
            col=0
            while col<a:
                if (row==0  and col!=a-1)or (row==a-1 and col!=a-1) or (col==0  and row!=a-1)or (col==a-1 and row!=0 and row<=a-1 and row!=a-1)or(row==col+a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()

    def S(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==0) or (row==col ) or (row==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()

    def T(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (col==a//2) or(row==0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()

    def U(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (col==0 and row!=a-1)or (row==a-1 and col!=0 and col!=a-1) or(col==a-1 and row!=a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()

    def V(self,a):
        row=0
        while row<a:
            col=0
            while col<a+a:
                if (row==col)or(row+col==a+a-2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()

    def W(self,a):
        row=0
        while row<a:
            col=0
            while col<a+a:
                if (col==0) or(row+col==a-1)or(col==row+a-1)or(col==a+a-2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
    def X(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row+col==a-1) or (row==col):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()


    def Y(self,a):
        row=0
        while row<a:
            col=0
            while col<a*2+2:
                if (row==col and col<a-a//2)+(row+col==a-1 and row<a-a//2)or (col==a-a%2-a//2 and row>a//2-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
    def Z(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==0) or(row+col==a-1)or (row==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()





            
            
            
            