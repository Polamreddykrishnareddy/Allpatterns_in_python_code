#Diamond symbols
print("Diamond symbols")
a=int(input("Enter the only odd numbers :"))
for row in range(a):
    for col in range(a):
        if  (col-row==a//2)or(col+row==a//2+a-1)or(row-col==a//2)or(col+row==a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    