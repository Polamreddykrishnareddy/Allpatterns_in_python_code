#v
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a:
        if (row+col==a-1 and row<a//2+1)or(row-col==0 and row<a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    