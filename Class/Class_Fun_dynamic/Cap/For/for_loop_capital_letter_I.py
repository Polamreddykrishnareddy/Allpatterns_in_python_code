#I
class capital_alphabets:
    def __init__(self):
        pass
    def I(self,a):
        for row in range(a):
            for col in range(a):
                if (col==a//2) or(row==0)or(row==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
