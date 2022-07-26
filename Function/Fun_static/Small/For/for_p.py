#p
def for_p(p,P):
    for row in range(p):#13
        for col in range(P):#6
            if (col==0 or row==0 and col!=5) or (row==1 and col==5)or (row==2 and col==5)or (row==3 and col==5)or (row==4 and col==5) or (row==5 and col!=5):#p
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

