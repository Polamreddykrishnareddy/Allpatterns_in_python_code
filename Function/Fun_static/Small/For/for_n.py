    #n
def for_n(n,N):
    for row in range(n):#5
        for col in range(N):#10
            if (col==1 and row>0)or(row-col==0 and row<1)or (row==0 and col<N//2 and col>1)or (col==N//2 and row>0)or (row==0 and col>N//2 and col<n):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

