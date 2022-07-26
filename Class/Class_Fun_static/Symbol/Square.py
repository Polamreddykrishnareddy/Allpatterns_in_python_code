#Square
class symbol:
    def __init__(self):
        pass
    def Square(self,a):
        print("Square")
        for row in range(a):
            for col in range(a):
                if (row==0) or (col==0)or(row==a-1)or(col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        
