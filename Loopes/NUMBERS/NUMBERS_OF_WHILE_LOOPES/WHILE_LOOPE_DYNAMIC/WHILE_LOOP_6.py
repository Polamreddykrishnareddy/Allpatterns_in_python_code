#6
a=int(input("Enter the number :"))
b=a+3
row=0
while row<b:
    col=0
    while col<a:
        if (row==b-1 and col>0 and col<a-1)or(row==b//2  and col>0 and col<a-1)or(col==0 and row>1 and  row<b-1)or(col==a-1 and row>b//2 and row<b-1)or(row==0 and col==2)or(row==1 and col==1):#6
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()