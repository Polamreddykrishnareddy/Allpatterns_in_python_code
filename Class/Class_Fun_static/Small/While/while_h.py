#h
class small_alphabits:
    def _-init__(self):
        pass
    def while_h(self,h,H):
        row=0
        while row<h:#11
            col =0
            while col<H:#10
                if (col==0) or (row==5 and col==1)or(row==5 and col==2)or(row==5 and col==3)or(row==5 and col==4)or(row==6 and col==5)or(row==7 and col==5)or(row==8 and col==5)or(row==9 and col==5)or(row==10 and col==5):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
