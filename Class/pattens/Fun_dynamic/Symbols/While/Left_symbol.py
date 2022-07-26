print("Left_symbol")
def Left_symbol(a):
    row=0
    while row<a:
        col=0
        while col<a:
            if (row-col==a//2)or(col+row==a//2)or(row==a//2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()

