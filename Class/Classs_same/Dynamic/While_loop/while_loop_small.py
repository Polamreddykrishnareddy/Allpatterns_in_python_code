class small_alphabets:
    def __init__(self):
        pass
    def a(self,b):
        a=3
        row=0
        while row<a+b:
            col=0
            while col<b:
                if(row==0 and col<b-2 and col>0)or(col==b-2 and row>0)or(row==1 and col==0)or(row==(a+b)-2 and col<b-1 and col>0)or(row==(a+b)//2-1 and col<b-1 and col>0)or(col==0 and row>b//2 and row<(a+b)-2) or(row==a+b-1 and col>b-2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
    def b(self,a):
        b=a+3
        row=0
        while row<b:
            col=0
            while col<a:
                if (col==0 and row<b-1)or(row==b//2 and col<a-1)or(row==b-1 and col>0 and col<a-1) or (col==a-1 and row>b//2 and row<b-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()            
            
    def c(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==0 and col>0) or(col==0 and row>0 and row<a-1) or(row==a-1 and col>0) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()            
    def d(self,a):
        b=a+a
        row=0
        while row<b:
            col=0
            while col<a:
                if (row==b//2 and col>0) or(col==0 and row>a and row<b-1) or(row==b-1 and col>0)or col==a-1 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
                        
    def e(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==0 and col>0 and col<a-1)or(row==a//2-1 and col<a-1) or(col==0 and row>0 and row<a-1) or(row==a-1 and col>0)or (col==a-1 and row>0 and row<a//2-1):#(col-row==a//2 and row<a//2-1)  :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()            
    def f(self,a):
        b=a+3
        row=0
        while row<b:
            col=0
            while col<a:
                if (col==a//2-1 and row>0)or (row==b//2) or row==0 and col>a//2-1 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
            
    def h(self,a):
        b=a+a
        row=0
        while row<b:
            col=0
            while col<a:
                if (col==0) or (row==b//2)or(col==a-1 and row>b//2) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()            
    def g(self,a):
        b=a+3
        row=0
        while row<b:
            col=0
            while col<a:
                if (col==a-1 ) or (row==0 and col>1) or(col==1 and row>0 and row<a//2)or(row==a//2 and col>1) or (row-col==3 and col>a//2-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
        
    def i(self,a):
        b=a+3
        row=0
        while row<b:
            col=0
            while col<a+1:
                if (col==a//2 and row>1)or (row==b-1) or(col==a//2+1 and row>1) or(row==0 and col>a//2-1 and col<a-1) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
    def j(self,a):
        b=a+3
        row=0
        while row<b:
            col=0
            while col<a:
                if  (col==a//2) or (row==0)or (row-col==a):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
                    
    def k(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if  (col==0) or (row-col==a//2-1) or (row+col==a//2+1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()            
            
    def l(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if( col==a//2) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
    def m(self,a):
        b=a+a
        row=0
        while row<a:
            col=0
            while col<b:
                if (col==1 and row>0)or(row-col==0 and row<1)or (row==0 and col<b//2 and col>1)or (col==b//2 and row>0)or (row==0 and col>b//2 and col<b-1)or(col==b-1 and row>0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
    def n(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (col==1 and row>0)or(row-col==0 and row<1) or (col==a-1 and row>0) or(row==0 and col<a-1 and col>1) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()                                    
    def o(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==0 and col>0 and col<a-1)or(row==a-1 and col>0 and col<a-1)or (col==0 and row>0 and row<a-1)or(col==a-1 and row>0 and row<a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
    def p(self,a):
        row=0
        while row<a+a:
            col=0
            while col<a:
                if (row==0 and col>0 and col<a-1)or(row==a-1 and col>0 and col<a-1)or (col==0)or(col==a-1 and row>0 and row<a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
    def q(self,a):
        row=0
        while row<a+3:
            col=0
            while col<a:
                if (row==0 and col>0 and col<a-1)or(row==a-1 and col>0 and col<a-1)or (col==0 and row>0 and row<a-1)or(col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
    def r(self,a):
        b=a+1
        row=0
        while row<b:
            col=0
            while col<a:
                if (row==col) or (row+col==a-1)or(row==a and col>0 and col<a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
    def s(self,a):
        b=a+a
        row=0
        while row<b:
            col=0
            while col<a:
                if  (row==0 and col>0) or (col==0 and row>0 and row<b//2-1) or(row==b//2-1 and col>0 and col<a-1) or(col==a-1 and row>a-1 and row<b-2)or(row==b-2 and col<a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
    def t(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (col==a//2)or(row==a//2-1)or(row==a-1 and col>a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
                                                
    def u(self,a):
        row=0
        while row<a+1:
            col=0
            while col<a+1:
                if (col==0 and row<a-1) or (col==a-1 and row<a ) or (row==a-1 and col>0 and col<a-1) or(row==a and col==a):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
            
    def v(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row+col==a-1 and row<a//2+1)or(row-col==0 and row<a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
                        
    def w(self,a):
        b=a+2
        row=0
        while row<b:
            col=0
            while col<b:
                if (col==0) or (row-col==0 and row>a//2) or(col==b-1) or(row+col==b-1 and row>a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
        
    def x(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==col) or (row+col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
    def y(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row-col==0 and col<a//2)or (row+col==a-1 ):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()            
    def z(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==0 )or (row+col==a-1 ) or(row==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
            
            
            
            
            
            
            
        

