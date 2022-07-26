#X
class capital_alphabets:
    def __init__(self):
        pass
    def X(self,a):
        for row in range(a):
            for col in range(a):
                if (row+col==a-1) or row==col:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
         
 
