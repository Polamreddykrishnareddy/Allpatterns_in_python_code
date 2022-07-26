#X
def X(a):
    for row in range(a):
        for col in range(a):
            if (row+col==a-1) or row==col:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
     
 
