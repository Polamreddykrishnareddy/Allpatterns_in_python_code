#I
class capital_alphabets:
    def __init__(self):
        pass
    def for_I(self,I,i):
        for row in range(6):
            for col in range(7):
                if row==0 or col==3 or row==5:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


