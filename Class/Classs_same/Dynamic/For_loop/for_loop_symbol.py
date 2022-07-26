class symbols:
    def __init__(self):
        pass
    
    def Addison(self,a):
        print("Addison")
        for row in range(a):
            for col in range(a):
                if (row==a//2)or(col==a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
            
           
    def Diamond_symbols(self,a):
        print("Diamond symbols")
        for row in range(a):
            for col in range(a):
                if  (col-row==a//2)or(col+row==a//2+a-1)or(row-col==a//2)or(col+row==a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    
    def Division(self,a):
        print("Division")
        for row in range(a):
            for col in range(a):
                if (row+col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()                    
    
    def Floor_division(self,a):
        print("Floor division")
        for row in range(a+1):
            for col in range(a+2):
                if (row+col==a-1)or(row+col==a+1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
            
    
    def Greater_than(self,a):
        print("Greater than")
        for row in range(a):
            for col in range(a):
                if  (col-row==a//2)or(col+row==a//2+a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
                    
    
    def Left_symbol(self,a):
        print("Less symbol")
        for row in range(a):
            for col in range(a):
                if (row-col==a//2)or(col+row==a//2)or(row==a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()            
            
    
    def Left_Triangle(self,a):
        print("Left Triangle")
        for row in range(a):
            for col in range(a):
                if (row==a-1 )or(row-col==0)or(col==0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()            
            
    
    def Lessthan(self,a):
        print("Less-than")
        for row in range(a):
            for col in range(a):
                if (row-col==a//2)or(col+row==a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
            
    
    def Multiplication(self,a):
        print("multiplication")
        for row in range(a):
            for col in range(a):
                if (row+col==a-1)or(row-col==0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    
    def Rectangle(self,a):
        print("Rectangle")
        for row in range(a):
            for col in range(a+3):
                if (row==0) or (col==0)or(row==a-1)or(col==a+2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()            
            
    
    def Right_symbol(self,a):
        print("Right symbol")
        for row in range(a):
            for col in range(a):
                if (row==a//2)or (col-row==a//2)or(col+row==a//2+a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
            
    
    def Right_Triangle(self,a):
        print("Right Triangle")
        for row in range(a):
            for col in range(a):
                if (row==a-1 )or(col+row==a-1)or(col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
   
    def Square(self,a):
        print("Square")
        for row in range(a):
            for col in range(a):
                if (row==0) or (col==0)or(row==a-1)or(col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
   
    def Subtraction(self,a):
        print("Subtraction")
        for row in range(a):
            for col in range(a+2):
                if (row==a//2) or (row==a-1)or(col==0 and row>a//2)or(col==a+1 and row>a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    
    def Triangle_or_parimetoer(self,a):
        print("Triangle")
        b=a+a
        for row in range(a):
            for col in range(b):
                if (row==a-1 and col<b-1)or(col+row==a-1)or(col-row==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
                                                
            
            
            
            
            