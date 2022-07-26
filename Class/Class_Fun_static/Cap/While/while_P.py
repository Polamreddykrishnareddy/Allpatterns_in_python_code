#P
class capital_alphabets:
    def __init__(self):
        pass
    def while_P(self,P,p):
        row=0
        while row<P:#11
            col =0
            while col<p:#7
                if (col==0) or (row==0 and col!=3 and col!=4 and col!=5 and col!=6)or (row==1 and col==3)or (row==2 and col==4 )or (row==3 and col==4)or (row==4 and col==3)or (row==5 and col==2)or (row==5 and col==1):

                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()


