#O
for row in range(5):
    for col in range(5):
        if (row==0 and col==1 ) or (row==0 and col==3 ) or (row==0 and col==2 ) or (col==0 and row!=0 and row!=4)or (row==4 and col!=0 and col!=4)or (col==4 and row!=0 and row!=4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
