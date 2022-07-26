#Multiplication
print("multiplication")
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a):
        if (row+col==a-1)or(row-col==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()