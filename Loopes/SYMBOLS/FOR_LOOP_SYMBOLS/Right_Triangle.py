#4. Right Triangle
print("Right Triangle")
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a):
        if (row==a-1 )or(col+row==a-1)or(col==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()