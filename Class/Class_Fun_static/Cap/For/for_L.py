#L
class capital_alphabets:
    def __init__(self):
        pass
    def for_L(self,L,l):
        for row in range(L):#8
            for col in range(l):#6
                if col==0 or row==7:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


