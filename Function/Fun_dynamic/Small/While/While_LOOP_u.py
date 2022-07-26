    #u
def u(a):
    row=0
    while row<a+1:
        col=0
        while col<a+1:
            if (col==0 and row<a-1) or (col==a-1 and row<a ) or (row==a-1 and col>0 and col<a-1) or(row==a and col==a):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()