a=int(input("Enter the  number :"))#X
for row in range(a):
    for col in range(a):
        if (row+col==a-1) or row==col:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
 
 