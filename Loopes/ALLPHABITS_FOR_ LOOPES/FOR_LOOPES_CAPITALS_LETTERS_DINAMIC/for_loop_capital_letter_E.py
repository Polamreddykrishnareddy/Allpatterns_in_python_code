a=int(input("Enter the  number :"))#E
for row in range(a):
    for col in range(a):
        if (row==0) or (row==a//2 )or (row==a-1)or(col==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    