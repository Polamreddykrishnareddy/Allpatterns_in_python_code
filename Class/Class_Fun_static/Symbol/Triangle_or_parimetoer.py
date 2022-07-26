#Triangle or parimetoer
class symbol:
    def __init__(self):
        pass
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
        
