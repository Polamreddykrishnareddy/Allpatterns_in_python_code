def for_f_parren(a):
    for row in range(9):
        for col in range(10):
            if (col==4 and row!=0)or (row==0 and col==5)or (row==0 and col==6)or (row==0 and col==7)or (row==4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_f_pattern(a):
    row=0
    while row<9:
        col =0
        while col<10:
            if (col==4 and row!=0)or (row==0 and col==5)or (row==0 and col==6)or (row==0 and col==7)or (row==4):

                print("*",end=" ")
            else:
                print(" ",end=" ")
            col +=1
        row +=1
        print()


