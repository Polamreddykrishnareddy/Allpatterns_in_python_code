#E
class capital_alphabets:
    def __init__(self):
        pass
    def E(self,a):
        for row in range(a):
            for col in range(a):
                if (row==0) or (row==a//2 )or (row==a-1)or(col==0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        
