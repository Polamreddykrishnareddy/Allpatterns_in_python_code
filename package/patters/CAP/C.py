#C
def for_C_pattern (b):
    for row in range(b):
        for col in range(b):
            if (col==0 and row!=0 and row!=b-1)or(row==0 and col!=0)or(row==b-1 and col!=0):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

    

#C
def while_C_pattern(b):
    row=0
    while row<b:
        col=0
        while col<b:
            if (col==0 and row!=0 and row!=b-1)or(row==0 and col!=0)or(row==b-1 and col!=0):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()

