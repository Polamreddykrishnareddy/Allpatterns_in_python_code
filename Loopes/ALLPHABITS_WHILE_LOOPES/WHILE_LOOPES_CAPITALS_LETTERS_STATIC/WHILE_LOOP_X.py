#X
row=0
while row<11:
    col =0
    while col<11:
        if (row==col) or (row==0 and col==10)or (row==1 and col==9)or (row==2 and col==8)or (row==3 and col==7)or (row==4 and col==6)or (row==6 and col==4)or (row==7 and col==3)or (row==8 and col==2)or (row==9 and col==1)or (row==10 and col==0):

            print("*",end=" ")
        else:
            print(" ",end=" ")
        col +=1
    row +=1
    print()
