#V
for row in range(6):
    for col in range(15):
        if (col==row)or (col+row==10):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
