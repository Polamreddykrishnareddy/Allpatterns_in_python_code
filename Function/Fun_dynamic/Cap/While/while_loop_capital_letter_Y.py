#Y
def Y(a):
    row=0
    while row<a:
        col=0
        while col<a*2+2:
            if (row==col and col<a-a//2)+(row+col==a-1 and row<a-a//2)or (col==a-a%2-a//2 and row>a//2-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
