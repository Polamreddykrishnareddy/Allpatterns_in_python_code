#y
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a):
        if (row-col==0 and col<a//2)or (row+col==a-1 ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()