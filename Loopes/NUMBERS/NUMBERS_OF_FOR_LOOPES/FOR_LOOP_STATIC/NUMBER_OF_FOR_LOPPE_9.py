#9
for row in range(10):
    for col in range(10):
        if (col==7 and row!=0) or (row==0 and col==6)or (row==0 and col==5)or (row==0 and col==4)or (row==1 and col==3) or (row==2 and col==3)or (row==3 and col==3)or(row==4 and col==4)or(row==4 and col==5)or (row==4 and col==6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
