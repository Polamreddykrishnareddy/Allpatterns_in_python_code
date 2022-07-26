print("Addison")
a=int(input("Enter the number:"))
row=0
while row<a:
    col=0
    while col<a:
        if (row==a//2)or(col==a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()

