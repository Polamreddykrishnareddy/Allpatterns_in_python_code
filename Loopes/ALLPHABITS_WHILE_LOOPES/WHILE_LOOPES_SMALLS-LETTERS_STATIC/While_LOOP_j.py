#j
row=0
while row<10:
    col =0
    while col<10:
        if (col==5 and row!=1)or (row==8 and col==4)or (row==7 and col==3):

            print("*",end=" ")
        else:
            print(" ",end=" ")
        col +=1
    row +=1
    print()
