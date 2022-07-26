#T
def for_T(T):
     for row in range(T):#7
        for col in range(T):#7
            if col==3 or row==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


