#H
def for_H(H,h):
    for  row in range(H):#7
        for col in range(h):#6
            if col==0 or col==5 or row==3 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


