    #4. Right Triangle
class symbol:
    def __init__(self):
        pass
    def Right_Triangle(self,a):
        print("Right Triangle")
        for row in range(a):
            for col in range(a):
                if (row==a-1 )or(col+row==a-1)or(col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
