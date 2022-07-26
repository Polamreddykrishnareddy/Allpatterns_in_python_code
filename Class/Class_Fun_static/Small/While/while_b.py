#b
class small_alphabits:
    def __init__(self):
        pass
    def while_b(self,b,B):
        row=0
        while row<b:#11
            col=0
            while col<B:#5
                if (col==0)or (row==6 and col==1)or (row==6 and col==2)or (row==6 and col==3)or (row==7 and col==4)or (row==8 and col==4)or (row==9 and col==4)or(row==10 and col==3)or(row==10 and col==2)or(row==10 and col==1) :

                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
