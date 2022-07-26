    # Left Triangle
class symbols:
    def __init__(self):
        pass    
    print("Left Triangle")
    def Left_Triangle(self,a):
        for row in range(a):
            for col in range(a):
                if (row==a-1 )or(row-col==0)or(col==0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        
