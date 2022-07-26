#t
def t(a):
    for row in range(a):
        for col in range(a):
            if (col==a//2)or(row==a//2-1)or(row==a-1 and col>a//2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()