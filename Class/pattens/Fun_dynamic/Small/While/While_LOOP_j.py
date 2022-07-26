    #j
def j(a):
    b=a+3
    row=0
    while row<b:
        col=0
        while col<a:
            if  (col==a//2) or (row==0)or (row-col==a):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()