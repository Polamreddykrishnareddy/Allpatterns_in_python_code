    #w
def for_w(w,W):
    for row in range(w):#7
        for col in range(W):#30
            if (col+row==12) or (row==col) or(col==row+12) or (col+row==24):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

