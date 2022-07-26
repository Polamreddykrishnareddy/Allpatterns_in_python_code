#Right Triangle
print("Right Triangle")
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a:
        if (row==a-1 )or(col+row==a-1)or(col==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
