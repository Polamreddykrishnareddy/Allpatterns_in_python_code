#A
def A(a):
    b=a+a
    row=0
    while row<a:
        col=0
        while col<b:
            if (row+col==a-1)or (col==row+a-1)or (row==a//2 and col>a//2-1 and col<a+a//2): 
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
