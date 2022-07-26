#10
a=int(input("Enter the number :"))
b=a+3
for row in range(a+3):
    for col in range(b):
        if (col==a//2)or(row==(a+2) and col<a)or(row+col==a//2)or(row==1 and col>b//2 and col<b-1)or(col==b-1 and row>1 and row<a) or(row==a and col>b//2 and col<b-1 )or(col==b//2 and row>1 and row<a):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()