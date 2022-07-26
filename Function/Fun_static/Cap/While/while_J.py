#J
def while_J(J,j):
    row=0
    while row<J:#6
        col =1
        while col<j:#7
            if (col==3 or row==0 ) or (row==4 and col==1)or (row==5 and col==2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col +=1
        row +=1
        print()


