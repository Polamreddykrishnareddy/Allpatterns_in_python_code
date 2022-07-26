#U
def for_U(S,s):
    for row in range(S):#6
        for col in range(s):#10
            if ( col==0 and row!=4 and row!=5) or(col==4 and row!=4 and row!=5)or (row==4 and col==1 ) or (row==4 and col==2)or (row==4 and col==3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


