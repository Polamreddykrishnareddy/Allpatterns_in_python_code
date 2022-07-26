#V
def V(a):
    for row in range(a):
        for col in range(a*2+2):
            if (row+col==a+a//2+a%2)or(row==col):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        
