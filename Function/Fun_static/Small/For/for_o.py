#o
def for_o(o):
    for row in range(o):#5
        for col in range(o):#5
            if (row==0 and col!=0 and col!=4) or (col==0 and row!=0 and row!=4) or (row==4 and col!=0 and col!=4) or (col==4 and row!=0 and row!=4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

