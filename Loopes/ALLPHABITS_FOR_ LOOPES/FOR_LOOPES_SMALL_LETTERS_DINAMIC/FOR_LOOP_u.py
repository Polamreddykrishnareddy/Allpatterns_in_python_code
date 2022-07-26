#u
a=int(input("Enter the number :"))
for row in range(a+1):
    for col in range(a+1):
        if (col==0 and row<a-1) or (col==a-1 and row<a ) or (row==a-1 and col>0 and col<a-1) or(row==a and col==a):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()