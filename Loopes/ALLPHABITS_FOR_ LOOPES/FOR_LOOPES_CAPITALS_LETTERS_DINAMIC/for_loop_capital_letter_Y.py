#Y
a=int(input("Enter the  only odd number :"))
for row in range(a):
    for col in range(a*2+2):
        if (row==col and col<a-a//2)+(row+col==a-1 and row<a-a//2)or (col==a-a%2-a//2 and row>a//2-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()