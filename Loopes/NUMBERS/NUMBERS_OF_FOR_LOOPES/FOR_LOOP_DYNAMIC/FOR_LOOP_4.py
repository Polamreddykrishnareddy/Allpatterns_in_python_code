#4
a=int(input("Enter the number :"))
for row in range(a+2):
    for col in range(a+1):
        if (col==a-1)or(row==a-1)or(row+col==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()