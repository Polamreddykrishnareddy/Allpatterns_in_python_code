#f
a=int(input("Enter the number :"))
b=a+3
row=0
while row<b:
    col=0
    while col<a:
        if (col==a//2-1 and row>0)or (row==b//2) or row==0 and col>a//2-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()