    #9
def _9(a):
    b=a+4
    for row in range(b):
        for col in range(a):
            if(row==0 and col>0 and col<a-1)or(row==b//2 and col>0 and col<a-1)or(col==a-1 and row>0)or(col==0 and row>0 and row<b//2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        