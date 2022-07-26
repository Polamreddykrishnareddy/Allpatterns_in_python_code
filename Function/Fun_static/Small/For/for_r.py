    #r
def for_r(r):
    for row in range(r):#10
        for col in range(r):#10
            if (col==1 and row!=0 )or(row==0 and col==0) or (row==1 and col==2)or (row==1 and col==3)or (row==1 and col==4)or (row==1 and col==5) or (row==2 and col==6)or (row==3 and col==7):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

