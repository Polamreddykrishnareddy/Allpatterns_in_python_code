def for_N(N):
    for row in range(N):
        for col in range(N):
            if (col==0) or (col==row) or (col==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()