
#P
def P(a):
    for row in range(a+5):
        for col in range(a):
            if (row==0  and col!=a-1)or (row==a-1 and col!=a-1) or (col==0  and row!=a-1)or (col==a-1 and row!=0 and row<=a-1 and row!=a-1 ):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
     
