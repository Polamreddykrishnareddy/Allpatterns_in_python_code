  #M 
b=int(input("Enter the name :"))
row=0
while row<b:
    col=0
    while col<b+b:
        if (col==0)or(row==col)or(row+col==b+b-2)or(col==b+b-2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()