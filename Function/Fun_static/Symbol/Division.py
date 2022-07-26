# Division
def Division(a):
    print("Division")
    for row in range(a):
        for col in range(a):
            if (row+col==a-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
