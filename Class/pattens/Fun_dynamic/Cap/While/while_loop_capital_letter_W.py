#W 
def W(a):
    row=0
    while row<a:
        col=0
        while col<a+a:
            if (col==0) or(row+col==a-1)or(col==row+a-1)or(col==a+a-2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
