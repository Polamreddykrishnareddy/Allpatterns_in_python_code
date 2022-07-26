#K
class capital_alphabets:
    def __init__(self):
        pass
    def K(self,a):
        for row in range(a):
            for col in range(a):
                if (col==0)or (row==col+a//2-1)or(row+col==a-a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

