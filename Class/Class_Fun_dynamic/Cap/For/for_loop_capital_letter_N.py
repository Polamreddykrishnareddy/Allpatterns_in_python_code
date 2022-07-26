#N
class capital_alphabets:
    def __init__(self):
        pass
    def N(self,a):
        for row in range(a):
            for col in range(a):
                if (col==0)or(row==col)or (col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
