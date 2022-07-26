#r
a=int(input("Enter the number :"))
b=a+1
for row in range(b):
    for col in range(a):
        if (row==col) or (row+col==a-1)or(row==a and col>0 and col<a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()