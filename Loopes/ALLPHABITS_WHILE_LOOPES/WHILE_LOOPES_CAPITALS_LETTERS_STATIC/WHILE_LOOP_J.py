#J
row=0
while row<6:
    col =1
    while col<7:
        if (col==3 or row==0 ) or (row==4 and col==1)or (row==5 and col==2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col +=1
    row +=1
