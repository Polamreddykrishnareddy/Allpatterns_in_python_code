    # Less-than
class symbols:
    def __init__(self):
        pass
    print("Less-than")
    def Lessthan(self,a):
        for row in range(a):
            for col in range(a):
                if (row-col==a//2)or(col+row==a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
