#m
class small_alphabits:
    def _-init__(self):
        pass
    def while_m(self,m,M):
        row=0
        while row<m:#5
            col =0
            while col<M:#10
                if (col==1 and row>0)or(row-col==0 and row<1)or (row==0 and col<M//2 and col>1)or (col==M//2 and row>0)or (row==0 and col>M//2 and col<M-1)or(col==M-1 and row>0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
