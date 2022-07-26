#l
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a):
        if( col==a//2) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    