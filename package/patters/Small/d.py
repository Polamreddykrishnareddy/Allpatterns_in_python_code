#d
def for_d_pattren(a):
    for row in range(10):
        for col in range(7):
            if (col==6 and row!=9)or (row==9 and col!=6 and col!=0)or (row==5 and col!=0) or (row==6 and col==0)or (row==7 and col==0)or (row==8 and col==0):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_d_pattern(a):
    row=0
    while row<10:
        col =0
        while col<7:
            if (col==6 and row!=9)or (row==9 and col!=6 and col!=0)or (row==5 and col!=0) or (row==6 and col==0)or (row==7 and col==0)or (row==8 and col==0):

                print("*",end=" ")
            else:
                print(" ",end=" ")
            col +=1
        row +=1
        print()


