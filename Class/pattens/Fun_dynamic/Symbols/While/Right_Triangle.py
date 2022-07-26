    #Right Triangle
print(" Right_Triangle")
def Right_Triangle(a):
    row=0
    while row<a:
        col=0
        while col<a:
            if (row==a-1 )or(col+row==a-1)or(col==a-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
