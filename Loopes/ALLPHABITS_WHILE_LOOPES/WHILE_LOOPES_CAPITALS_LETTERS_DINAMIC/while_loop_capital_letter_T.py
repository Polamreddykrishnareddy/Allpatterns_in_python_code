 #T
a=int(input("Enter the name :"))
row=0
while row<a:
    col=0
    while col<a:
        if (col==a//2) or(row==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()