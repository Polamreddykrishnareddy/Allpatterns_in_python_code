    #4. Right Triangle
class symbols:
    def __init__(self):
        pass
    print("Right Triangle")
    def Right_Triangle(self,a):
        for row in range(a):
            for col in range(a):
                if (row==a-1 )or(col+row==a-1)or(col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
