#V
def for_V(V,v):
    for row in range(V):#6
        for col in range(v):#15
            if (col==row)or (col+row==10):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


