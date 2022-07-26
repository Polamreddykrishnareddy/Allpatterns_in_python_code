    # Subtraction
print("Subtraction")
def Subtraction(a):
    for row in range(a):
        for col in range(a+2):
            if (row==a//2) or (row==a-1)or(col==0 and row>a//2)or(col==a+1 and row>a//2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        