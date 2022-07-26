
#U
class capital_alphabets:
    def __init__(self):
        pass
    def U(self,a):
        for row in range(a):
            for col in range(a):
                if (col==0 and row!=a-1)or (row==a-1 and col!=0 and col!=a-1) or(col==a-1 and row!=a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
