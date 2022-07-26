#L
row=0
while row<8:
    col =0
    while col<6:
        if col==0 or row==7:            
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col +=1
    row +=1
    print()
