#H
a=int(input("Enter the name :"))
row=0
while row<a:
    col=0
    while col<a:
        if (row==a//2) or (col==0) or (col==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()