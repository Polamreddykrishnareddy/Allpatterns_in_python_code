#q
class small_alphabits:
    def _-init__(self):
        pass
    def while_q(self,q,Q):
        row=0
        while row<q:#13
            col =0
            while col<Q:#6
                if (col==5 or row==0 and col!=0 and col!=6 and col!=7) or (row==1 and col==0)or (row==2 and col==0)or (row==3 and col==0)or (row==4 and col==0) or (row==5 and col!=0 and col!=6 and col!=7) or (row==11 and col==6) or (row==10 and col==7):#p

                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
