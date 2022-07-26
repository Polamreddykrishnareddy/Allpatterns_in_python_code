def for_D_pattern (b):
    for row in range(b):
        for col in range(b):
            if (col==0)or(row==0 and 2<b and col!=b-1 and col!=b-2)or(row==b-1 and 2<b and col!=b-1 and col!=b-2)or(col==b-2 and row!=0 and row!=b-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        
def while_D_pattern(b):
    row=0
    while row<b:
        col=0
        while col<b:
            if (col==0)or(row==0 and 2<b and col!=b-1 and col!=b-2)or(row==b-1 and 2<b and col!=b-1 and col!=b-2)or(col==b-2 and row!=0 and row!=b-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()

