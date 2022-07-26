#W
row=0
while row<6:
    col =0
    while col<18:
        if (col==row)or (row==4 and col==6)or (row==3 and col==7)or (row==2 and col==8)or (row==3 and col==9)or (row==4 and col==10)or (row==5 and col==11) or(row+col==16):

            print("*",end=" ")
        else:
            print(" ",end=" ")
        col +=1
    row +=1
    print()
