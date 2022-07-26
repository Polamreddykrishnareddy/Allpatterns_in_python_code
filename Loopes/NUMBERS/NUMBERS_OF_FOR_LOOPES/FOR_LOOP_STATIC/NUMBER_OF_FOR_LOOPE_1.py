#1 NUMBER_OF_FOR_LOOPE_1
for row in range(10):
    for col in range(10):
        if (col==5) or(row==1 and col==4)or(row==2 and col==3) or (row==3 and col==2)or (row==9):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
