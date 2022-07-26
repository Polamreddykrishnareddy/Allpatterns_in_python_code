    #4
def for_4(a,b):
    for row in range(a):#10
        for col in range(b):#9
            if col+row==6 or row==6 or (col==6):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


