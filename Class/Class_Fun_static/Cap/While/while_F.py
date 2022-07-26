#F
class capital_alphabets:
    def __init__(self):
        pass
    def while_F(self,F,f):
        row=0
        while row<F:#7
            col =0
            while col<f:#4
                if col==0 or row==0 or row==3:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()


