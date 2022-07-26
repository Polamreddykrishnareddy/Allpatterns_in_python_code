    #O
def while_O(O):
    row=0
    while row<O:#5
        col =0
        while col<O:#5
            if (row==0 and col==1 ) or (row==0 and col==3 ) or (row==0 and col==2 ) or (col==0 and row!=0 and row!=4)or (row==4 and col!=0 and col!=4)or (col==4 and row!=0 and row!=4):

                print("*",end=" ")
            else:
                print(" ",end=" ")
            col +=1
        row +=1
        print()


