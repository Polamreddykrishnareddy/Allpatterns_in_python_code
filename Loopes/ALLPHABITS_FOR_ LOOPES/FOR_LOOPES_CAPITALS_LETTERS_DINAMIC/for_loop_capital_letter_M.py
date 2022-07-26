
a=int(input("Enter the number :"))#M
c=a+a
b=c-2
for row in range(a):
    for col in range(b):
        if (col==0)or(row==col)or(row+col==b>8-1)or (col==b-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
