# Floor division
print("Floor division")
def Floor_division(a):
    for row in range(a+1):
        for col in range(a+2):
            if (row+col==a-1)or(row+col==a+1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        