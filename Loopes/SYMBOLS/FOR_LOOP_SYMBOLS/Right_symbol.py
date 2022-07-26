#Right symbol
print("Right symbol")
a=int(input("Enter the only odd numbers :"))
for row in range(a):
    for col in range(a):
        if (row==a//2)or (col-row==a//2)or(col+row==a//2+a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()