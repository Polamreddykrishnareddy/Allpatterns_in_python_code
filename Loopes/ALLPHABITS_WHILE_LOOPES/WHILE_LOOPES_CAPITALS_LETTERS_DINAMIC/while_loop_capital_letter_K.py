   
#K
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a:
        if (col==0)or (row==col+a//2-1)or(row+col==a-a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()