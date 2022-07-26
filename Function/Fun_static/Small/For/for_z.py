#z
def for_z(z):
    for row in range(z):#6
        for col in range(z):#6
            if (row==0) or (col+row==5) or (row==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

