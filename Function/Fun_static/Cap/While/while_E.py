    #E
def while_E(E,e):
    row=0
    while row<E:#7
        col =0
        while col<e:#6
            if col==0 or row==0 or row==3 or row==6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col +=1
        row +=1
        print()


