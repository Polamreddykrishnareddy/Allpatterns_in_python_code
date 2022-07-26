#t
for row in range(9):#tttttt
    for col in range(9):
        if (col==4) or (row==2) or (row==8 and col!=0 and col!=1 and col!=2 and col!=3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
