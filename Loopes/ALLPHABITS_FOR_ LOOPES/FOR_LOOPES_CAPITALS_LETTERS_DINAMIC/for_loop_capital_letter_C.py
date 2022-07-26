
#C
b=int(input("Enter the row and col :"))#C
for row in range(b):
    for col in range(b):
        if (col==0 and row!=0 and row!=b-1)or(row==0 and col!=0)or(row==b-1 and col!=0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    