#1
def _1(a):
    for row in range(a+2):
        for col in range(a):
            if (col==a//2)or(row==a+1)or(row+col==a//2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()