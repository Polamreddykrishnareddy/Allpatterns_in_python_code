#C
def C(b):
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
