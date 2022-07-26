#y
class small_alphabits:
    def _-init__(self):
        pass
    def while_y(self,y,Y):
        row=0
        while row<y:#10
            col=0
            while col<Y:#9
                if (row+col==8 ) or (row==0 and col==0) or (row==1 and col==1)or (row==2 and col==2)or (row==3 and col==3)or (row==4 and col==4) or (row==7 and col==0)or(row==6 and col==0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
