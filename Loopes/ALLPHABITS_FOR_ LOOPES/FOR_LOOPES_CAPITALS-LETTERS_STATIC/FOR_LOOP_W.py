#W
for row in range(6):
    for col in range(18):
        if (col==row)or (row==4 and col==6)or (row==3 and col==7)or (row==2 and col==8)or (row==3 and col==9)or (row==4 and col==10)or (row==5 and col==11) or(row+col==16):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
