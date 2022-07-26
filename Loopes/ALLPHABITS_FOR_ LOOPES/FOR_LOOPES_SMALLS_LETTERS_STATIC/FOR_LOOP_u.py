#u
for row in range(7):
    for col in range(7):###uuuuuuuuuvvvvvv
        if (col==0 and row!=6) or (col==5  and row!=6 ) or (row==6 and col==1) or (row==6 and col==2) or (row==6 and col==3) or (row==6 and col==4)or(row==6 and col==6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
