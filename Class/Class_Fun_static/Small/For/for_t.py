    #t
class small_alphabits:
    def __init__(self):
        pass
    def for_t(self,t):
        for row in range(t):#9
            for col in range(t):#9
                if (col==4) or (row==2) or (row==8 and col!=0 and col!=1 and col!=2 and col!=3):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

