#w
def while_w(w,W):
    row=0
    while row<w:#7
        col =0
        while col<W:#30
            if (col+row==12) or (row==col) or(col==row+12) or (col+row==24):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col +=1
        row +=1
        print()
