#d
class small_alphabits:
    def _-init__(self):
        pass
    def while_d(self,d,D):
        row=0
        while row<d:#10
            col =0
            while col<D:#7
                if (col==6 and row!=9)or (row==9 and col!=6 and col!=0)or (row==5 and col!=0) or (row==6 and col==0)or (row==7 and col==0)or (row==8 and col==0):

                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
