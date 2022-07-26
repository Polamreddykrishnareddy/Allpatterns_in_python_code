#T
class capital_alphabets:
    def __init__(self):
        pass
    def while_T(self,T):
        row=0
        while row<T:#7
            col =0
            while col<T:#7
                if col==3 or row==0:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()


