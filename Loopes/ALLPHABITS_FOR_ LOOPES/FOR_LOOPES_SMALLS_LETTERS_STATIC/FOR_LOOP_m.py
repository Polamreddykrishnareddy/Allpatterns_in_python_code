#m
for row in range(7):
    for col in range(10):
        if (col==1 and row!=0 or row==0 and col==0 or col==5 and row!=0 or row==1 and col!=0 or col==9 and row!=0  ):###mmmm
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
