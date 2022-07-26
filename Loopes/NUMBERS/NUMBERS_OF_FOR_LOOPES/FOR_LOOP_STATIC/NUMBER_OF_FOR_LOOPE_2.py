#2 
for row in range(10):
    for col in range(10):
        if (row==9 )or (col+row==9 and row!=0 and row!=2 and row!=1)or (row==2 and col==6)or (row==1 and col==6)or (row==0 and col==5)or (row==0 and col==4)or (row==0 and col==3)or (row==1 and col==2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
