#r
a=int(input("Enter the number :"))
b=a+1
row=0
while row<b:
    col=0
    while col<a:
        if (row==col) or (row+col==a-1)or(row==a and col>0 and col<a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
