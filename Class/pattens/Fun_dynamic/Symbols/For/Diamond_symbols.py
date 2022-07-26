    #Diamond symbols
def Diamond_symbols(a):
    print("Diamond symbols")
    for row in range(a):
        for col in range(a):
            if  (col-row==a//2)or(col+row==a//2+a-1)or(row-col==a//2)or(col+row==a//2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        