#c
def for_a_pattern(a):
    for row in range(7):
        for col in range(7):
            if  (row==0 and col!=0) or (col==0 and row!=0 and row!=7 and row!=6)or (row==6 and col!=0):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_c_pattern(a):
    row=0
    while row<7:
        col =0
        while col<7:
            if  (row==0 and col!=0) or (col==0 and row!=0 and row!=7 and row!=6)or (row==6 and col!=0):

                print("*",end=" ")
            else:
                print(" ",end=" ")
            col +=1
        row +=1
        print()



