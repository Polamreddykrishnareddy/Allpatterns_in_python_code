#L
def for_L(L,l):
    for row in range(L):#8
        for col in range(l):#6
            if col==0 or row==7:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


