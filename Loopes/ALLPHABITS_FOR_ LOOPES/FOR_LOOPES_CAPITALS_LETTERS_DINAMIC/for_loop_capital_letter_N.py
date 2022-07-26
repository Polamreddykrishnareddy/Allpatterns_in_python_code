a=int(input("Enter the  number :"))#N
for row in range(a):
    for col in range(a):
        if (col==0)or(row==col)or (col==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()