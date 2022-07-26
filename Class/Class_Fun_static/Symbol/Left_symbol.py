#Left symbol
class symbol:
    def __init__(self):
        pass
    def Left_symbol(self,a):
        print("Left symbol")
        for row in range(a):
            for col in range(a):
                if (row-col==a//2)or(col+row==a//2)or(row==a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
