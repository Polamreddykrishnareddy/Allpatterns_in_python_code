# v 
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a):
        if (row+col==a-1 and row<a//2+1)or(row-col==0 and row<a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()