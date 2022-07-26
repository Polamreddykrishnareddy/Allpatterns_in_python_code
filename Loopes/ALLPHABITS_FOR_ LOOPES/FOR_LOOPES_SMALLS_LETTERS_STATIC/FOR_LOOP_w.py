#w
for row in range(7):
    for col in range(30):
        if (col+row==12) or (row==col) or(col==row+12) or (col+row==24):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
