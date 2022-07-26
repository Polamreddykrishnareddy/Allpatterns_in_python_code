    #j
def for_j(j):
    for row in range(j):#10
        for col in range(j):#10
            if (col==5 and row!=1)or (row==8 and col==4)or (row==7 and col==3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

