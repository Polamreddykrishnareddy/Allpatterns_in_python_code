#I
def while_I(I,i):
    row=0
    while row<I:#6
        col =0
        while col<i:#7
            if row==0 or col==3 or row==5:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col +=1
        row +=1
        print()


