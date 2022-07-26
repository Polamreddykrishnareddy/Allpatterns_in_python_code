    #Q
def while_Q(Q):
    row=0
    while row<Q:#8
        col =0
        while col<Q:#8
            if (col==1 and row==0)or (col==2 and row==0)or (col==3 and row==0)or (col==4 and row==1)or (col==4 and row==2)or (col==4 and row==3)or (col==5 and row==5)or (col==6 and row==6)or (col==1 and row==4)or (col==2 and row==4)or (col==3 and row==4)or (col==4 and row==4)or (col==0 and row==1)or (col==0 and row==2)or (col==0 and row==3)or (col==3 and row==3)or (col==2 and row==2):

                print("*",end=" ")
            else:
                print(" ",end=" ")
            col +=1
        row +=1
        print()


