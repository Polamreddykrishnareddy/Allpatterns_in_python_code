    #x
class small_alphabits:
    def __init__(self):
        pass
    def for_x(self,x,X):
        for row in range(x):#10
            for col in range(X):#11
                if (col==row) or (row+col==9):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

