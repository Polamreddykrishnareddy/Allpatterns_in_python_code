    #6
def _6(a):
    b=a+3
    for row in range(b):
        for col in range(a):
            if (row==b-1 and col>0 and col<a-1)or(row==b//2  and col>0 and col<a-1)or(col==0 and row>1 and  row<b-1)or(col==a-1 and row>b//2 and row<b-1)or(row==0 and col==2)or(row==1 and col==1):#6
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        