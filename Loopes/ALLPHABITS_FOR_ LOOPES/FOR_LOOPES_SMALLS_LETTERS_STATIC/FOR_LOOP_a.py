#a
for row in range(10):
    for col in range(10):
        if  (col==5 and row!=0 and row!=1) or(row==2 and col==2)or (row==1 and col==4) or (row==1 and col==3) or (row==5 and col==4) or (row==5 and col==3) or (row==6 and col==2) or (row==7 and col==2) or (row==8 and col==3)or (row==8 and col==4) or (row==9 and col==6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
