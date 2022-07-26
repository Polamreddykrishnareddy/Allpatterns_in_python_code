#d
def d(a):
    b=a+a
    row=0
    while row<b:
        col=0
        while col<a:
            if (row==b//2 and col>0) or(col==0 and row>a and row<b-1) or(row==b-1 and col>0)or col==a-1 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
        