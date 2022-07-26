#Less symbol
print("Less symbol")
a=int(input("Enter the only odd numbers :"))
for row in range(a):
    for col in range(a):
        if (row-col==a//2)or(col+row==a//2)or(row==a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()