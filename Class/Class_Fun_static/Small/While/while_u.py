#u
class small_alphabits:
    def _-init__(self):
        pass
    def while_u(self,u,U):
        row=0
        while row<u:#7
            col =0
            while col<U:#8
                if (col==0 and row!=6) or (col==5  and row!=6 ) or (row==6 and col==1) or (row==6 and col==2) or (row==6 and col==3) or (row==6 and col==4)or(row==6 and col==6):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
