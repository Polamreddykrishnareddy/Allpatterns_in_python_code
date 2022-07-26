#T
class capital_alphabets:
    def __init__(self):
        pass
    def for_T(self,T):
         for row in range(T):#7
            for col in range(T):#7
                if col==3 or row==0:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


