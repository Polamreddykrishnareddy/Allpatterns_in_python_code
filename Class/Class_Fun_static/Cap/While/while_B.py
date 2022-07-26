#B
class capital_alphabets:
    def __init__(self):
        pass
    def while_B(self,B,b):
        row=0
        while row<B:#7
            col =0
            while col<b:#6
                if (col==0)or(row==0 and col!=5)or(row==1 and col==5) or (row==2 and  col==5)  or (row==3 and col!=5)  or  (row==6 and col!=5)or (row==4 and col==5)or (row==5 and col==5): 
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()

