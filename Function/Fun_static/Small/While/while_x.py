#x
def while_x(x,X):
    row=0
    while row<x:#10
        col=0
        while col<X:#11
            if col==row or row+col==8:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col +=1
        row +=1
        print()
