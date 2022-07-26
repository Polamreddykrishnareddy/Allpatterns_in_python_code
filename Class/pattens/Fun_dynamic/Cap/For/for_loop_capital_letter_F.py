#F
def F(a):
    for row in range(a):
        for col in range(a):
            if (row==0 and col<a-2) or (row==a//2-1 and col<a-2)or(col==0 ):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
