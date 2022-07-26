  #Z
a=int(input("Enter the name :"))
row=0
while row<a:
    col=0
    while col<a:
        if (row==0) or(row+col==a-1)or (row==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()