# Floor division
print("Floor division")
a=int(input("Enter the number :"))
for row in range(a+1):
    for col in range(a+2):
        if (row+col==a-1)or(row+col==a+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    