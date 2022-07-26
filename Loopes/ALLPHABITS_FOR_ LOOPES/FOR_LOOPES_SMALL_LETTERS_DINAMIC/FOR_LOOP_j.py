#j
a=int(input("Enter the number :"))
b=a+3
for row in range(b):
    for col in range(a):
        if  (col==a//2) or (row==0)or (row-col==a):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    