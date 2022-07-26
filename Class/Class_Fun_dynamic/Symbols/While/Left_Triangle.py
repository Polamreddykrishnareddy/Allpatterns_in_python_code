    # Left Triangle
class symbols:
    def __init__(self):
        pass
    print("Left_Triangle")
    def Left_Triangle(self,a):
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
