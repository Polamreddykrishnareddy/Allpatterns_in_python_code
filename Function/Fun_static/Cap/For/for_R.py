#R
def for_R(R,r):
    for row in range(R):#11
        for col in range(r):#6
            if (col==0) or (row==0 and col!=3 and col!=4 and col!=5 and col!=6)or (row==1 and col==3)or (row==2 and col==4 )or (row==3 and col==4)or (row==4 and col==3)or (row==5 and col==2)or (row==5 and col==1)or (row==col+5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


