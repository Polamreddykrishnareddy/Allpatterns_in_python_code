#k
row=0
while row<15:
    col =0
    while col<20:
        if (col==0)or (row==col+8)or (row==8 and col==2)or (row==7 and col==3)or (row==6 and col==4)or (row==5 and col==5)or (row==4 and col==6) :

            print("*",end=" ")
        else:
            print(" ",end=" ")
        col +=1
    row +=1
    print()
