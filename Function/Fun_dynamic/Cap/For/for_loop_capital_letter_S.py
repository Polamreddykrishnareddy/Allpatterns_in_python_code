
#S
def S(a):
    for row in range(a):
        for col in range(a):
            if (row==0) or (row==col ) or (row==a-1):
                 print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        
