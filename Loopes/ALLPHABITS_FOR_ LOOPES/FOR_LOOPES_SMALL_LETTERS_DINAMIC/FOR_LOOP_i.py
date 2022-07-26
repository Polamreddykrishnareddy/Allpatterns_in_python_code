#i
a=int(input("Enter the number :"))
b=a+3
for row in range(b):
    for col in range(a+1):
        if (col==a//2 and row>1)or (row==b-1) or(col==a//2+1 and row>1) or(row==0 and col>a//2-1 and col<a-1) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    