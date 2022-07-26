#N
def while_N(N):
    row=0
    while row<N:#6
        col =0
        while col<N:#6
            if (col==0) or (col==row) or (col==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col +=1
        row +=1
        print()


