#c
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a):
        if (row==0 and col>0) or(col==0 and row>0 and row<a-1) or(row==a-1 and col>0) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()