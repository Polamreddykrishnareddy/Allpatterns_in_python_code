#Y
a=int(input("Enter the number :"))
if a%2==1:
    for row in range(a):
        for col in range(a*2+2):
            if (row==col and col<a-a//2)+(row+col==a-1 and row<a-a//2)or (col==a-a%2-a//2 and row>a//2-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
elif a%2==0:
    for row in range(a):
        for col in range(a*2+2):
            if (row==col and col<a-a//2)+(row+col==a and row<a-a//2)or (col==a-a%2-a//2 and row>a//2-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
