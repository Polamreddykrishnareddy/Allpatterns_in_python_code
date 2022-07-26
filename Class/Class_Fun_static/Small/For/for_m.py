    #m
class small_alphabits:
    def __init__(self):
        pass
    def for_m(self,m,M):
        for row in range(m):#5
            for col in range(M):#10
                if (col==1 and row>0)or(row-col==0 and row<1)or (row==0 and col<M//2 and col>1)or (col==M//2 and row>0)or (row==0 and col>M//2 and col<M-1)or(col==M-1 and row>0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

