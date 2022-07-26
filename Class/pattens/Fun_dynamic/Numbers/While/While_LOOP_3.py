    #3
def _3(a):
    b=a+a
    row=0
    while row<b:
        col=0
        while col<a:
            if (row==0 and col<a-1)or(row==b//2 and col<a-1)or(row==b-1 and col<a-1)or(col==a-1 and row!=a and row>0 and row<b-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
        