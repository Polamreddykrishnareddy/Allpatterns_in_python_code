#V
row=0
while row<6:
    col =0
    while col<15:
        if (col==row)or (col+row==10):

            print("*",end=" ")
        else:
            print(" ",end=" ")
        col +=1
    row +=1
    print()
