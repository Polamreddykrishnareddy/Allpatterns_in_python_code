#v
class small_alphabits:
    def __init__(self):
        pass
    def for_v(self,v,V):
        for row in range(v):#7
            for col in range(V):#15
                if (col+row==12) or (row==col):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

