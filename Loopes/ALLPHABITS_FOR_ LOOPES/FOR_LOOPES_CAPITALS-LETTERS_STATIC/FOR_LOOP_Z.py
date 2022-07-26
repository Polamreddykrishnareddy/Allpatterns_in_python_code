#Z
for row in range(12):
    for col in range(10):
        if (row==0)or(row+col==9)or (row==9) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 
