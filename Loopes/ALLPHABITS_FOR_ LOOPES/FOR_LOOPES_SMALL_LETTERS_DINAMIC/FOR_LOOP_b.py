#b
a=int(input("Enter the number :"))
b=a+3
for row in range(b):
    for col in range(a):
        if (col==0 and row<b-1)or(row==b//2 and col<a-1)or(row==b-1 and col>0 and col<a-1) or (col==a-1 and row>b//2 and row<b-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    