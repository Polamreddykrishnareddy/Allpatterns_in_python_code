# Rectangle
print("Rectangle")
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a+3):
        if (row==0) or (col==0)or(row==a-1)or(col==a+2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()