#a
b=int(input("Enter the number :"))
a=3
row=0
while row<a+b:
    col=0
    while col<b:
        if(row==0 and col<b-2 and col>0)or(col==b-2 and row>0)or(row==1 and col==0)or(row==(a+b)-2 and col<b-1 and col>0)or(row==(a+b)//2-1 and col<b-1 and col>0)or(col==0 and row>b//2 and row<(a+b)-2) or(row==a+b-1 and col>b-2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    