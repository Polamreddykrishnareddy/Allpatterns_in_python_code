    #5
def _5(a):
    b=a+a
    for row in range(b):
        for col in range(a):
            if (row==0)or(col==0 and row<a-1)or(row==a-1 and col<a-1)or(col==a-1 and row>a-1 and row<b-1)or(row==b-1 and col<a-1):#5
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        