#x
for row in range(10):
    for col in range(11):
        if col==row or row+col==9:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
