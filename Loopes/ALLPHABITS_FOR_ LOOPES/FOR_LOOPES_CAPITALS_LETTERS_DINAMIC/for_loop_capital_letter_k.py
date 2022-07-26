a=int(input("Enter the  number :"))#K
for row in range(a):
    for col in range(a):
        if (col==0)or (row==col+a//2-1)or(row+col==a-a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
