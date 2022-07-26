    #Multiplication
print("multiplication")
def Multiplication(a):
    for row in range(a):
        for col in range(a):
            if (row+col==a-1)or(row-col==0):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()