#13. Greater than
class symbols:
    def __init__(self):
        pass
    
    def Greater_than(self,a):
        print("Greater than")
        for row in range(a):
            for col in range(a):
                if  (col-row==a//2)or(col+row==a//2+a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        
