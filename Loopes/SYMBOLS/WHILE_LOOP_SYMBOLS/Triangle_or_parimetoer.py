#Triangle or parimetoer 
print("Triangle or parimetoer ")
a=int(input("Enter the number :"))
b=a+a
row=0
while row<a:
    col=0
    while col<b:
        if (row==a-1 and col<b-1)or(col+row==a-1)or(col-row==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
