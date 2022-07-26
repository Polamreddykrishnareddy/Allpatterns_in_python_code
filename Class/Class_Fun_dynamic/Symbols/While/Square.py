    #1.Square
class symbols:
    def __init__(self):
        pass
    print("Square")
    def Square(self,a):
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
