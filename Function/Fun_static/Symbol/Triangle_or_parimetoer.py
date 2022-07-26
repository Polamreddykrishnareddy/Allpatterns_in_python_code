#Triangle or parimetoer
def Triangle_or_parimetoer(a): 
    print("Triangle")
    b=a+a
    for row in range(a):
        for col in range(b):
            if (row==a-1 and col<b-1)or(col+row==a-1)or(col-row==a-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        
