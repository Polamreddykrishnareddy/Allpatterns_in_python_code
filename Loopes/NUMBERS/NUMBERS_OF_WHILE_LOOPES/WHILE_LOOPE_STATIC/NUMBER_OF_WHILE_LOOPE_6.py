#6 
row=0
while row<8:
    col=0
    while col<20:
        if (col==0 and row!=7 and row!=0 and row!=1) or (row==0 and col==2) or(row==1 and col==1)or (row==7 and col==1)or (row==7 and col==2)or (row==7 and col==3)or (row==6 and col==4)or (row==5 and col==4)or (row==4 and col==3) or (row==4 and col==1) or (row==4 and col==2):
       
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col +=1
    row +=1
    print()    
