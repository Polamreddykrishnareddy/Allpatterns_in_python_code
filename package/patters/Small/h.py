def for_h_pattern(a):
    for row in range(11):#    hhhhhhhhhhhhhhhhhhh
        for col in range(10):
            if (col==0) or (row==5 and col==1)or(row==5 and col==2)or(row==5 and col==3)or(row==5 and col==4)or(row==6 and col==5)or(row==7 and col==5)or(row==8 and col==5)or(row==9 and col==5)or(row==10 and col==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def while_h_pattern(a):
    row=0
    while row<11:
        col =0
        while col<10:
            if (col==0) or (row==5 and col==1)or(row==5 and col==2)or(row==5 and col==3)or(row==5 and col==4)or(row==6 and col==5)or(row==7 and col==5)or(row==8 and col==5)or(row==9 and col==5)or(row==10 and col==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col +=1
        row +=1
        print()

