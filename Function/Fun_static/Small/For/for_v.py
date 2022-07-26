#v
def for_v(v,V):
    for row in range(v):#7
        for col in range(V):#15
            if (col+row==12) or (row==col):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

