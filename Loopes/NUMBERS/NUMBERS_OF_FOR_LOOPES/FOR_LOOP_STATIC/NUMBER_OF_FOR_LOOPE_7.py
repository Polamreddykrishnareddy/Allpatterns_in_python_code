#7
for row in range(10):
    for col in range(10):
        if col+row==9 or row==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
