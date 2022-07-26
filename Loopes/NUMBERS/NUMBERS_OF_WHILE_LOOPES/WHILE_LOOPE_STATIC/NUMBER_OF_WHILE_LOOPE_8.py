#8 
row=0
while row<11:
    col=0
    while col<6:
        if (row==0 and col!=0 and col!=5) or (col==0 and row!=10 and row!=0 and col!=5 and row!=5)or (row==5 and col==1)or (row==5 and col==2)or (row==5 and col==3)or (row==5 and col==4) or(col==5  and row!=10 and row!=5 and row!=0)or (row==10 and col==1)or (row==10 and col==2)or (row==10 and col==3)or (row==10 and col==4):

            print("*",end=" ")
        else:
            print(" ",end=" ")
        col +=1
    row +=1
    print()
    
