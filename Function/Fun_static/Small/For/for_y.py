#y
def for_y(y,Y):
    for row in range(y):#10
        for col in range(Y):#9
            if (row+col==8 ) or (row==0 and col==0) or (row==1 and col==1)or (row==2 and col==2)or (row==3 and col==3)or (row==4 and col==4) or (row==7 and col==0)or(row==6 and col==0):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

