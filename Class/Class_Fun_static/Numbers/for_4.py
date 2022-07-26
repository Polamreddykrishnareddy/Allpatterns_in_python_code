    #4
class numbers:
    def __init__(self):
        pass
    def for_4(self,a,b):
        for row in range(a):#10
            for col in range(b):#9
                if col+row==6 or row==6 or (col==6):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


