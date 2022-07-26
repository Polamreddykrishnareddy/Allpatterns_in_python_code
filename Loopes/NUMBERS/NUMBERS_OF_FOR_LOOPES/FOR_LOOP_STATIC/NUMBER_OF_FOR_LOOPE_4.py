#4
for row in range(10):
    for col in range(9):
        if col+row==6 or row==6 or (col==6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
