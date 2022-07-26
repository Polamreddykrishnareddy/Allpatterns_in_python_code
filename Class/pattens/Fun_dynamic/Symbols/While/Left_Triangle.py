    # Left Triangle
print("Left_Triangle")
def Left_Triangle(a):
    row=0
    while row<a:
        col=0
        while col<a:
            if (row==a-1 )or(row-col==0)or(col==0):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()