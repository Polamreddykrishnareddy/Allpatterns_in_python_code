    #2
def _2(a):
    b=a+2
    row=0
    while row<b:
        col=0
        while col<a:
            if (row==0 and col>1 and col<a-1)or(row==a//2+1 and col>1 and col<a-1)or(col==1 and row>0 and row<a//2+1)or(col==a-1 and row>0 and row<a//2+1)or(row+col==a+1)or(row==a+1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
        