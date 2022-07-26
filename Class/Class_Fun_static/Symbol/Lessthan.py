# Less-than
class symbol:
    def __init__(self):
        pass
    def Lessthan(self,a):
        print("Less-than")
        for row in range(a):
            for col in range(a):
                if (row-col==a//2)or(col+row==a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
