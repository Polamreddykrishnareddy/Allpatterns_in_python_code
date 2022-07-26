    #Triangle or parimetoer
class symbols:
    def __init__(self):
        pass
    print("Triangle")
    def Triangle_or_parimetoer(self,a):
        b=a+a
        for row in range(a):
            for col in range(b):
                if (row==a-1 and col<b-1)or(col+row==a-1)or(col-row==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
            
