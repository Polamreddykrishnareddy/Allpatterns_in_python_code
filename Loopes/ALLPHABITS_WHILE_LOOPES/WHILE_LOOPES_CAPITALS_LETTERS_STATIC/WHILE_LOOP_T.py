#T
row=0
while row<7:
    col =0
    while col<7:
        if col==3 or row==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col +=1
    row +=1
    print()
