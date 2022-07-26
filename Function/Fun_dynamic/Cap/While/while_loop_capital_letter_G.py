#G
def G(b):
    row=0
    while row<b:
        col=0
        while col<b:
            if (col==0 and row!=0 and row!=b-1 and row!=b-2)or(row==0 and col!=0)or(row==b-2 and col!=0)or(col==b-1 and row>b//2-1)or(row==b//2 and col>1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
