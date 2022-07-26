    #l
class small_alphabits:
    def __init__(self):
        pass
    def for_l(self,l):
        for row in range(l):#6
            for col in range(l):#6
                if col==4 or col==5:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

