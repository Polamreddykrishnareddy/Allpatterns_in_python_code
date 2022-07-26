#v
def while_v(v,V):
    row=0
    while row<v:#7
        col =0
        while col<V:#15
            if (col+row==12) or (row==col):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col +=1
        row +=1
        print()
