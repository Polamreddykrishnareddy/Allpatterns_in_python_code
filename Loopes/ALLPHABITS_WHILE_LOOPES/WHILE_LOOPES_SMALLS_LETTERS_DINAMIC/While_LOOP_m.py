#m
a=int(input("Enter the number :"))
b=a+a
row=0
while row<a:
    col=0
    while col<b:
        if (col==1 and row>0)or(row-col==0 and row<1)or (row==0 and col<b//2 and col>1)or (col==b//2 and row>0)or (row==0 and col>b//2 and col<b-1)or(col==b-1 and row>0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    