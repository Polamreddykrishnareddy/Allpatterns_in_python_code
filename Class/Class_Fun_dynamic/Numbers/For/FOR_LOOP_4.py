    #4
class Numbers:
    def __init__(self):
        pass
    def _4(self,a):
        for row in range(a+2):
            for col in range(a+1):
                if (col==a-1)or(row==a-1)or(row+col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
