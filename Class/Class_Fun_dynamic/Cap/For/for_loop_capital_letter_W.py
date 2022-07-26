#W
class capital_alphabets:
    def __init__(self):
        pass
    def W(self,a):
        for row in range(a):
            for col in range(a+a):
                if (col==0) or(row+col==a-1)or(col==row+a-1)or(col==a+a-2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
