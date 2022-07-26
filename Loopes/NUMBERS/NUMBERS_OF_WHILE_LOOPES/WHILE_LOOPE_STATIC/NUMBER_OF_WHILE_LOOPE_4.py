#4 
row=0
while row<10:
    col=0
    while col<9:
        if col+row==6 or row==6 or (col==6):

            print("*",end=" ")
        else:
            print(" ",end=" ")
        col +=1
    row +=1
    print()
