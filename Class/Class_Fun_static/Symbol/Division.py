# Division
class symbol:
    def __init__(self):
        pass
    def Division(self,a):
        print("Division")
        for row in range(a):
            for col in range(a):
                if (row+col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
