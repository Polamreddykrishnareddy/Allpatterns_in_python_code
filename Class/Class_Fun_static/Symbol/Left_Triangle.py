# Left Triangle
class symbol:
    def __init__(self):
        pass
    def Left_Triangle(self,a):
        print("Left Triangle")
        for row in range(a):
            for col in range(a):
                if (row==a-1 )or(row-col==0)or(col==0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
            
