    #Right symbol
def Right_symbol(a):
    print("Right symbol")
    for row in range(a):
        for col in range(a):
            if (row==a//2)or (col-row==a//2)or(col+row==a//2+a-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
