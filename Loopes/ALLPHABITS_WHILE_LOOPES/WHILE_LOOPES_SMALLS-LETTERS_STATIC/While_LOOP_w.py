#w
row=0
while row<7:
    col =0
    while col<30:
        if (col+row==12) or (row==col) or(col==row+12) or (col+row==24):

            print("*",end=" ")
        else:
            print(" ",end=" ")
        col +=1
    row +=1
    print()
