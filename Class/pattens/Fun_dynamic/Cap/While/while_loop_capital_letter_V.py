#V 
def V(a):
    row=0
    while row<a:
        col=0
        while col<a+a:
            if (row==col)or(row+col==a+a-2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
