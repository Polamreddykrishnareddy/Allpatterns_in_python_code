#2. Rectangle
print("Rectangle")
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a+3:
        if (row==0) or (col==0)or(row==a-1)or(col==a+2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()