    #e
def for_e(e):
    for row in range(e):#7
        for col in range(e):#7
            if  (row==0 and col!=0) or (col==0 and row!=0 and row!=7 and row!=6)or (row==6 and col!=0) or (row==2 and col==1)or (row==2 and col==2)or (row==2 and col==5)or  (row==2 and col==3)or (row==2 and col==4)or (row==1 and col==6):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

