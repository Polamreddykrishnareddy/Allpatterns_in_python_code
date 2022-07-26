#K
row=0
while row<8:
    col =0
    while col<9:
        if (col==0 or row==col+3)or (col==1 and row==3)or(row==2 and col==2)or (row==1 and col==3) or (row==0 and col==4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col +=1
    row +=1
    print()
