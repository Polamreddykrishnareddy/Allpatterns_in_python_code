#o
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a:
        if (row==0 and col>0 and col<a-1)or(row==a-1 and col>0 and col<a-1)or (col==0 and row>0 and row<a-1)or(col==a-1 and row>0 and row<a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()