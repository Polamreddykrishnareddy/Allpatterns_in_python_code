#L
class capital_alphabets:
    def __init__(self):
        pass
    def while_L(self,L,l):
        row=0
        while row<L:#8
            col =0
            while col<l:#6
                if col==0 or row==7:            
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()


