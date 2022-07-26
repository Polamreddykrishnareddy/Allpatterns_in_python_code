#m
row=0
while row<7:
    col =0
    while col<10:
        if (col==1 and row!=0 or row==0 and col==0 or col==5 and row!=0 or row==1 and col!=0 or col==9 and row!=0  ):###mmmm

            print("*",end=" ")
        else:
            print(" ",end=" ")
        col +=1
    row +=1
    print()
