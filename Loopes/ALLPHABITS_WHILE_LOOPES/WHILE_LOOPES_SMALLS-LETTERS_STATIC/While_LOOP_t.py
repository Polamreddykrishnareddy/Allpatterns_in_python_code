#t
row=0
while row<9:
    col =0
    while col<9:
        if (col==4) or (row==2) or (row==8 and col!=0 and col!=1 and col!=2 and col!=3):

            print("*",end=" ")
        else:
            print(" ",end=" ")
        col +=1
    row +=1
    print()
