#l
for row in range(10):
    for col in range(10):
        if col==5 or col==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
