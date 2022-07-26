    #Right Triangle
class symbols:
    def __init__(self):
        pass
    print(" Right_Triangle")
    def Right_Triangle(self,a):
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
