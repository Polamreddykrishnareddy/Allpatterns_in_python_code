    #7
class Numbers:
    def __init__(self):
        pass
    def _7(self,a):
        for row in range(a):
            for col in range(a):
                if (row==0)or(row+col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
