#N
row=0
while row<6:
    col =0
    while col<6:
        if (col==0) or (col==row) or (col==5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col +=1
    row +=1
    print()
