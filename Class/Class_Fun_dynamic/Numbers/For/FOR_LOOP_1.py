#1
class Numbers:
    def __init__(self):
        pass
    def _1(self,a):
        for row in range(a+2):
            for col in range(a):
                if (col==a//2)or(row==a+1)or(row+col==a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
