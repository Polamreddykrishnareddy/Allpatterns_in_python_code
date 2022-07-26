#V
class capital_alphabets:
    def __init__(self):
        pass
    def for_V(self,V,v):
        for row in range(V):#6
            for col in range(v):#15
                if (col==row)or (col+row==10):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


