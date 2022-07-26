#H
class capital_alphabets:
    def __init__(self):
        pass
    def H(self,a):
        for row in range(a):
            for col in range(a):
                if (row==a//2) or (col==0) or (col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

