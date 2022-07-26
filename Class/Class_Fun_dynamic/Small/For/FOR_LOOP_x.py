#x
class Small_alphabets:
    def __init__(self):
        pass 
    def x(self,a):
        for row in range(a):
            for col in range(a):
                if (row==col) or (row+col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        
