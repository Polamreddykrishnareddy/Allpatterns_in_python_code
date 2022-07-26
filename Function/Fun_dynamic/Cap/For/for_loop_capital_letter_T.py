
#T  
def T(a):
    for row in range(a):
        for col in range(a):
            if (col==a//2) or(row==0):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
     
