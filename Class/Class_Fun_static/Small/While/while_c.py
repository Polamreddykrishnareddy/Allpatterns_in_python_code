#c
class small_alphabits:
    def _-init__(self):
        pass
    def while_c(self,c): 
        row=0
        while row<c:#7
            col =0
            while col<c:#7
                if (row==0 and col!=0) or (col==0 and row!=0 and row!=7 and row!=6)or (row==6 and col!=0):

                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
