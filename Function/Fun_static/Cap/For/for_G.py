#G
def for_G(G):
    for row in range(G):#6
        for col in range(G):#6
            if (col==0 and row!=0)or(row==0 and col==1)or(row==0 and col==2) or (row==3 and col!=1) or (col==5 and row!=0 and row!=1 and row!=2) or(row==4 and col==3) or (row==5 and col!=4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


