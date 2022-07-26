#i
for row in range(10):
    for col in range(10):
        if (col==5 and row!=1)or (col==6 and row!=1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

