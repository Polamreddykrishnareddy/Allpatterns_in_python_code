#F
class capital_alphabets:
    def __init__(self):
        pass
    def for_F(self,F,f):
        for row in range(F):#7
            for col in range(f):#6
                if col==0 or row==0 or row==3:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


