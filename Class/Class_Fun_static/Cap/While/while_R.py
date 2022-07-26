    #R
class capital_alphabets:
    def __init__(self):
        pass
    def while_R(self,R,r):
        row=0
        while row<R:#11
            col =0
            while col<r:#6
                if (col==0) or (row==0 and col!=3 and col!=4 and col!=5 and col!=6)or (row==1 and col==3)or (row==2 and col==4 )or (row==3 and col==4)or (row==4 and col==3)or (row==5 and col==2)or (row==5 and col==1)or (row==col+5):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()


