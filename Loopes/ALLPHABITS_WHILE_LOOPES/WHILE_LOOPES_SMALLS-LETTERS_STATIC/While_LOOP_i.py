#i
row=0
while row<10:
    col =0
    while col<10:
        if (col==5 and row!=1)or (col==6 and row!=1):

            print("*",end=" ")
        else:
            print(" ",end=" ")
        col +=1
    row +=1
    print()
