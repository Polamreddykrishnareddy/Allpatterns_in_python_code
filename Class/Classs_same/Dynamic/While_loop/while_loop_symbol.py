class symbols:
    def __init__(self):
        pass    
    
    def Addison(self,a):
        print("Addison")
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==a//2)or(col==a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()

    def Diamond_symbols(self,a):
        print("Diamond symbols")
        row=0
        while row<a:
            col=0
            while col<a:
                if  (col-row==a//2)or(col+row==a//2+a-1)or(row-col==a//2)or(col+row==a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()


    def Division(self,a):
        print("Division")
        row=0
        while row<a:
            col=0
            while col<a:
                if (row+col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()            
            
 
    def Floor_division(self,a):
        print("Floor_division")
        row=0
        while row<a:
            col=0
            while col<a:
                if (row+col==a-1)or(row+col==a+1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
           

    def Greater_than(self,a):
        print("Greater_than")
        row=0
        while row<a:
            col=0
            while col<a:
                if  (col-row==a//2)or(col+row==a//2+a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()            
            

    def Left_symbol(self,a):
        print("Left_symbol")
        row=0
        while row<a:
            col=0
            while col<a:
                if (row-col==a//2)or(col+row==a//2)or(row==a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()            
            
 
    def Left_Triangle(self,a):
        print("Left_Triangle")
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==a-1 )or(row-col==0)or(col==0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()            
            

    def Lessthan(self,a):
        print("Less-than")
        row=0
        while row<a:
            col=0
            while col<a:
                if (row-col==a//2)or(col+row==a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()


    def Multiplication(self,a):
        print("Multiplication")
        row=0
        while row<a:
            col=0
            while col<a:
                if (row+col==a-1)or(row-col==0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()

    def Rectangle(self,a):
        print("Rectangle")
        row=0
        while row<a:
            col=0
            while col<a+3:
                if (row==0) or (col==0)or(row==a-1)or(col==a+2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()


    def Right_symbol(self,a):
        print("Right_symbol")
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==a//2)or (col-row==a//2)or(col+row==a//2+a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
            

    def Right_Triangle(self,a):
        print(" Right_Triangle")
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==a-1 )or(col+row==a-1)or(col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
            

    def Square(self,a):
        print("Square")
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==0) or (col==0)or(row==a-1)or(col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()            
            
            

    def Subtraction(self,a):
        print("Subtraction")
        row=0
        while row<a:
            col=0
            while col<a+2:
                if (row==a//2) or (row==a-1)or(col==0 and row>a//2)or(col==a+1 and row>a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
            

    def Triangle_or_parimetoer(self,a):
        print("Triangle or parimetoer ")
        b=a+a
        row=0
        while row<a:
            col=0
            while col<b:
                if (row==a-1 and col<b-1)or(col+row==a-1)or(col-row==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()            
            
            
            
            

