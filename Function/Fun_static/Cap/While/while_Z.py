    #Z
def while_Z(Z,z):
    row=0
    while row<Z:#12
        col =0
        while col<z:#10
            if (row==0)or(row+col==9)or (row==9) :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col +=1
        row +=1
        print()


