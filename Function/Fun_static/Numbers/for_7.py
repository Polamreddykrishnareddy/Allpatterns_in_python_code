#7
def for_7(_7):
    for row in range(_7):#10
        for col in range(_7):#10
            if col+row==6 or row==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


