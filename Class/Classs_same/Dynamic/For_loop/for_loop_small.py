class Small_alphabets:
    def __init__(self):
        pass
    def a(self,b):
        a=3
        for row in range(a+b):
            for col in range(b):
                if(row==0 and col<b-2 and col>0)or(col==b-2 and row>0)or(row==1 and col==0)or(row==(a+b)-2 and col<b-1 and col>0)or(row==(a+b)//2-1 and col<b-1 and col>0)or(col==0 and row>b//2 and row<(a+b)-2) or(row==a+b-1 and col>b-2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def b(self,a):
        b=a+3
        for row in range(b):
            for col in range(a):
                if (col==0 and row<b-1)or(row==b//2 and col<a-1)or(row==b-1 and col>0 and col<a-1) or (col==a-1 and row>b//2 and row<b-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()            
            
    def c(self,a):
        for row in range(a):
            for col in range(a):
                if (row==0 and col>0) or(col==0 and row>0 and row<a-1) or(row==a-1 and col>0) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
            
    def d(self,a):
        b=a+a
        for row in range(b):
            for col in range(a):
                if (row==b//2 and col>0)or(col==0 and row>a and row<b-1) or(row==b-1 and col>0)or col==a-1 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def e(self,a):
        for row in range(a):
            for col in range(a):
                if (row==0 and col>0 and col<a-1)or(row==a//2-1 and col<a-1) or(col==0 and row>0 and row<a-1) or(row==a-1 and col>0)or (col==a-1 and row>0 and row<a//2-1):#(col-row==a//2 and row<a//2-1)  :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
            
    def f(self,a):
        b=a+3
        for row in range(b):
            for col in range(a):
                if (col==a//2-1 and row>0)or (row==b//2) or row==0 and col>a//2-1 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
            
    def g(self,a):
        b=a+3
        for row in range(b):
            for col in range(a):
                if (col==a-1 ) or (row==0 and col>1) or(col==1 and row>0 and row<a//2)or(row==a//2 and col>1) or (row-col==3 and col>a//2-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def h(self,a):
        b=a+a
        for row in range(b):
            for col in range(a):
                if (col==0) or (row==b//2)or(col==a-1 and row>b//2) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()            
    def i(self,a):
        b=a+3
        for row in range(b):
            for col in range(a+1):
                if (col==a//2 and row>1)or (row==b-1) or(col==a//2+1 and row>1) or(row==0 and col>a//2-1 and col<a-1) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
                    
    def j(self,a):
        b=a+3
        for row in range(b):
            for col in range(a):
                if  (col==a//2) or (row==0)or (row-col==a):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def k(self,a):
        for row in range(a):
            for col in range(a):
                if  (col==0) or (row-col==a//2-1) or (row+col==a//2+1):
                #if  (col==0) or (row-col==a//2) or (row+col==a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
                        
    def l(self,a):
        for row in range(a):
            for col in range(a):
                if( col==a//2) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
            
    def m(self,a):
        b=a+a
        for row in range(a):
            for col in range(b):
                if (col==1 and row>0)or(row-col==0 and row<1)or (row==0 and col<b//2 and col>1)or (col==b//2 and row>0)or (row==0 and col>b//2 and col<b-1)or(col==b-1 and row>0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
                        
    def n(self,a):
        for row in range(a):
            for col in range(a):
                if (col==1 and row>0)or(row-col==0 and row<1) or (col==a-1 and row>0) or(row==0 and col<a-1 and col>1) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def o(self,a):
        for row in range(a):
            for col in range(a):
                if (row==0 and col>0 and col<a-1)or(row==a-1 and col>0 and col<a-1)or (col==0 and row>0 and row<a-1)or(col==a-1 and row>0 and row<a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def p(self,a):
        for row in range(a+a):
            for col in range(a):
                if (row==0 and col>0 and col<a-1)or(row==a-1 and col>0 and col<a-1)or (col==0)or(col==a-1 and row>0 and row<a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
            
    def q(self,a):
        for row in range(a+3):
            for col in range(a):
                if (row==0 and col>0 and col<a-1)or(row==a-1 and col>0 and col<a-1)or (col==0 and row>0 and row<a-1)or(col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()                        
            
            
    def r(self,a):
        b=a+1
        for row in range(b):
            for col in range(a):
                if (row==col) or (row+col==a-1)or(row==a and col>0 and col<a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
            
    def s(self,a):
        b=a+a
        for row in range(b):
            for col in range(a):
                if  (row==0 and col>0) or (col==0 and row>0 and row<b//2-1) or(row==b//2-1 and col>0 and col<a-1) or(col==a-1 and row>a-1 and row<b-2)or(row==b-2 and col<a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()            
            
    def t(self,a):
        for row in range(a):
            for col in range(a):
                if (col==a//2)or(row==a//2-1)or(row==a-1 and col>a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
            
    def u(self,a):
        for row in range(a+1):
            for col in range(a+1):
                if (col==0 and row<a-1) or (col==a-1 and row<a ) or (row==a-1 and col>0 and col<a-1) or(row==a and col==a):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()           
    def v(self,a):
        for row in range(a):
            for col in range(a):
                if (row+col==a-1 and row<a//2+1)or(row-col==0 and row<a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()            
            
    def w(self,a):
        b=a+2
        for row in range(b):
            for col in range(b): 
                if (col==0) or (row-col==0 and row>a//2) or(col==b-1) or(row+col==b-1 and row>a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()           
            
    def x(self,a):
        for row in range(a):
            for col in range(a):
                if (row==col) or (row+col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
                    
    def y(self,a):
        for row in range(a):
            for col in range(a):
                if (row-col==0 and col<a//2)or (row+col==a-1 ):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()            
            
    def z(self,a):
        for row in range(a):
            for col in range(a):
                if (row==0 )or (row+col==a-1 ) or(row==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
                    