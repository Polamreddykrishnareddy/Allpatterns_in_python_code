#I
def I(a):
    for row in range(a):
        for col in range(a):
            if (col==a//2) or(row==0)or(row==a-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
