#v
row=0
while row<7:
    col =0
    while col<15:
        if (col+row==12) or (row==col):

            print("*",end=" ")
        else:
            print(" ",end=" ")
        col +=1
    row +=1
    print()
