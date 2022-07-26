#z
def while_z(z):
    row=0
    while row<z:#10
        col=0
        while col<z:#10
            if (row==0) or (col+row==8) or (row==8):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col +=1
        row +=1
        print()
