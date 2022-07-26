    #4
def _4(a):
    for row in range(a+2):
        for col in range(a+1):
            if (col==a-1)or(row==a-1)or(row+col==a-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()