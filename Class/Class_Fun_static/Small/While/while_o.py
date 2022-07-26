#o
class small_alphabits:
    def _-init__(self):
        pass
    def while_o(self,o):
        row=0
        while row<o:#5
            col =0
            while col<o:#5
                if (row==0 and col!=0 and col!=4) or (col==0 and row!=0 and row!=4) or (row==4 and col!=0 and col!=4) or (col==4 and row!=0 and row!=4):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
