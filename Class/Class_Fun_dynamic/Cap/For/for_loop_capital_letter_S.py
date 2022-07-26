
#S
class capital_alphabets:
    def __init__(self):
        pass
    def S(self,a):
        for row in range(a):
            for col in range(a):
                if (row==0) or (row==col ) or (row==a-1):
                     print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
            
