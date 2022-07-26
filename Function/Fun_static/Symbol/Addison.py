# Addison
def Addison(a):
    print("Addison")
    for row in range(a):
        for col in range(a):
            if (row==a//2)or(col==a//2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        
