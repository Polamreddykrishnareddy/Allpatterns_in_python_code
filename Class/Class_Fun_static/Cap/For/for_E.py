#E
class capital_alphabets:
    def __init__(self):
        pass
    def for_E(self,E,e):
        for row in range(E):#7
            for col in range(e):#6
                if col==0 or row==0 or row==3 or row==6:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


