#n
class small_alphabits:
    def _-init__(self):
        pass
    def while_n(self,n,N):
        row=0
        while row<n:#5
            col =0
            while col<N:#10
                if (col==1 and row>0)or(row-col==0 and row<1)or (row==0 and col<N//2 and col>1)or (col==N//2 and row>0)or (row==0 and col>N//2 and col<n):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
