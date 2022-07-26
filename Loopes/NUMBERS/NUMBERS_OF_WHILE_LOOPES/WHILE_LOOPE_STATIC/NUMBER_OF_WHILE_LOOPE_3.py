#  3 
row=0
while row<8:
    col=0
    while col<6:
        if (row==0) or (row==1 and col==4) or (row==2 and col==3)or (row==3 and col==2)or (row==4 and col==3)or (row==5 and col==4) or row==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col +=1
    row +=1
    print()
