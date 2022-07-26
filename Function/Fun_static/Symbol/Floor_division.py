# Floor division
def Floor_division(a):
    print("Floor division")
    for row in range(a+1):
        for col in range(a+2):
            if (row+col==a-1)or(row+col==a+1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        
