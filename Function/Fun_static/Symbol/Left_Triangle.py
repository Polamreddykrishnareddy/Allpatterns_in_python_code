# Left Triangle
def Left_Triangle(a):
    print("Left Triangle")
    for row in range(a):
        for col in range(a):
            if (row==a-1 )or(row-col==0)or(col==0):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        
