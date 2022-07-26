def for_e_pattern(a):
    for row in range(10):
        for col in range(10):
            if (col==9 and row!=0)or (row==9 and col==8)or (row==8 and col==7) or (row==0 and col==8)or (row==0 and col==7)or (row==0 and col==6)or (row==0 and col==5) or (row==1 and col==4)or (row==2 and col==4)or (row==3 and col==4)or (row==4 and col==5) or (row==4 and col==6) or (row==4 and col==7) or (row==4 and col==8):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_g_pattern(a):
    row=0
    while row<10:
        col =0
        while col<10:
            if (col==9 and row!=0)or (row==9 and col==8)or (row==8 and col==7) or (row==0 and col==8)or (row==0 and col==7)or (row==0 and col==6)or (row==0 and col==5) or (row==1 and col==4)or (row==2 and col==4)or (row==3 and col==4)or (row==4 and col==5) or (row==4 and col==6) or (row==4 and col==7) or (row==4 and col==8):

                print("*",end=" ")
            else:
                print(" ",end=" ")
            col +=1
        row +=1
        print()


