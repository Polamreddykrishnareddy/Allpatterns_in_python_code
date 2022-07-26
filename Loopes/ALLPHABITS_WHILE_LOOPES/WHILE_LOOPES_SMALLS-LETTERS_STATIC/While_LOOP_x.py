#x
row=0
while row<10:
    col =0
    while col<11:
        if col==row or row+col==9:

            print("*",end=" ")
        else:
            print(" ",end=" ")
        col +=1
    row +=1
    print()
