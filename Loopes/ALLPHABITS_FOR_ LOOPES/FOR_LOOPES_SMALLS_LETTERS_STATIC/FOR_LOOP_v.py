#v
for row in range(7):
    for col in range(15):
        if (col+row==12) or (row==col):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
