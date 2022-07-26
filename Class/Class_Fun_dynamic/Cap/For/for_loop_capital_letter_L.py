#L
class capital_alphabets:
    def __init__(self):
        pass
    def L(self,a):
        for row in range(a):
            for col in range(a):
                if (col==0)or(row==a-1 and col!=a-1 and col!=a-2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


