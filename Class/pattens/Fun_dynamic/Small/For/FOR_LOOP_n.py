#n
def n(a):
    for row in range(a):
        for col in range(a):
            if (col==1 and row>0)or(row-col==0 and row<1) or (col==a-1 and row>0) or(row==0 and col<a-1 and col>1) :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()