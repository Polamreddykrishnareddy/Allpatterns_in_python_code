#F
def for_F(F,f):
    for row in range(F):#7
        for col in range(f):#6
            if col==0 or row==0 or row==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


