    #x
def for_x(x,X):
    for row in range(x):#10
        for col in range(X):#11
            if (col==row) or (row+col==9):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

